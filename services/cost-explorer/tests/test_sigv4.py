"""AWS SigV4 single-chunk signing tests.

Vectors come from two sources:

* The AWS documentation page ``reference_sigv-create-signed-request``
  (the canonical "Examples of the complete version 4 signing process"
  walkthrough). These provide end-to-end Authorization headers.
* The AWS published test-suite credentials
  (AKID ``AKIDEXAMPLE`` / secret ``wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY``,
  date ``20150830``, region ``us-east-1``, service ``service``) which
  AWS uses to verify SigV4 implementations across SDKs.
"""

from __future__ import annotations

import pytest

from pywhatwgurl import URL
from zapros import Headers, Request

from aws_sdk_cost_explorer._auth._sigv4 import (
    SigV4AuthContext,
    _build_canonical_request,
    _canonical_headers,
    _canonical_path,
    _canonical_query,
    _derive_signing_key,
    _trim_header_value,
    _uri_encode,
    sign_sigv4,
)


# ---------------------------------------------------------------------------
# Helper-level tests
# ---------------------------------------------------------------------------


class TestUriEncode:
    def test_unreserved_passthrough(self):
        assert _uri_encode("abcABC0123-_.~") == "abcABC0123-_.~"

    def test_space_becomes_percent20(self):
        assert _uri_encode("a b") == "a%20b"

    def test_slash_is_encoded(self):
        # SigV4 encodes "/" in query keys/values; only the path treats "/" as safe.
        assert _uri_encode("a/b") == "a%2Fb"

    def test_reserved_encoded(self):
        # `=`, `&`, `+` must all be percent-encoded in canonical query.
        assert _uri_encode("a=b&c+d") == "a%3Db%26c%2Bd"

    def test_unicode_utf8(self):
        # é → 0xC3 0xA9 → %C3%A9
        assert _uri_encode("é") == "%C3%A9"


class TestCanonicalPath:
    def test_empty_becomes_root(self):
        assert _canonical_path("", service="s3") == "/"
        assert _canonical_path("", service="iam") == "/"

    def test_s3_passthrough(self):
        # S3 must NOT normalize or re-encode the path.
        assert (
            _canonical_path("/my-bucket/key%20with%20space", service="s3")
            == "/my-bucket/key%20with%20space"
        )

    def test_s3_preserves_double_slash(self):
        assert _canonical_path("/a//b", service="s3") == "/a//b"

    def test_non_s3_double_encodes(self):
        # "/foo bar" → first encode → "/foo%20bar" → second → "/foo%2520bar"
        assert _canonical_path("/foo bar", service="iam") == "/foo%2520bar"

    def test_non_s3_already_encoded_double_encodes(self):
        # "/foo%20bar" gets unquoted to "/foo bar", then double-encoded.
        assert _canonical_path("/foo%20bar", service="iam") == "/foo%2520bar"


class TestCanonicalQuery:
    def test_empty(self):
        assert _canonical_query("") == ""
        assert _canonical_query("?") == ""

    def test_sorted_by_key(self):
        assert _canonical_query("b=2&a=1") == "a=1&b=2"

    def test_value_encoded(self):
        assert _canonical_query("a=hello world") == "a=hello%20world"

    def test_dup_keys_sorted_by_value(self):
        # SigV4 spec: when keys collide, sort by value as well.
        assert _canonical_query("a=2&a=1") == "a=1&a=2"

    def test_key_without_value(self):
        # The S3 "?lifecycle" form: bare key produces "key=".
        assert _canonical_query("lifecycle") == "lifecycle="

    def test_strips_leading_question_mark(self):
        assert _canonical_query("?a=1") == "a=1"


class TestTrimHeaderValue:
    def test_strip(self):
        assert _trim_header_value("  hello  ") == "hello"

    def test_collapse_internal(self):
        assert _trim_header_value("a   b") == "a b"

    def test_combined(self):
        assert _trim_header_value("  a    b  c  ") == "a b c"


class TestCanonicalHeaders:
    def test_lowercased_and_sorted(self):
        h = Headers({"Host": "example.com", "X-Amz-Date": "20150830T123600Z"})
        canonical, signed = _canonical_headers(h)
        assert signed == "host;x-amz-date"
        assert canonical == "host:example.com\nx-amz-date:20150830T123600Z\n"

    def test_excludes_unsigned_set(self):
        h = Headers(
            {
                "Host": "example.com",
                "User-Agent": "boto/x",
                "Authorization": "old",
                "X-Amzn-Trace-Id": "trace",
            }
        )
        _, signed = _canonical_headers(h)
        assert signed == "host"

    def test_multi_value_comma_joined(self):
        h = Headers([("Host", "example.com"), ("X-My", "a"), ("X-My", "b")])
        canonical, signed = _canonical_headers(h)
        assert signed == "host;x-my"
        assert "x-my:a,b\n" in canonical


# ---------------------------------------------------------------------------
# Signing-key derivation — AWS docs published intermediate values
# ---------------------------------------------------------------------------


def test_derive_signing_key_matches_aws_doc_example():
    """Reference: AWS SigV4 "Examples of deriving a signing key" page.

    secret = wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY
    date   = 20120215
    region = us-east-1
    service= iam
    -> kSigning hex:
       f4780e2d9f65fa895f9c67b32ce1baf0b0d8a43505a000a1a9e090d414db404d
    """
    key = _derive_signing_key(
        "wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY",
        "20120215",
        "us-east-1",
        "iam",
    )
    assert (
        key.hex() == "f4780e2d9f65fa895f9c67b32ce1baf0b0d8a43505a000a1a9e090d414db404d"
    )


# ---------------------------------------------------------------------------
# End-to-end signing — AWS test-suite vectors
# ---------------------------------------------------------------------------


_TEST_SUITE_CTX: SigV4AuthContext = {
    "type": "sig_v4",
    "access_key_id": "AKIDEXAMPLE",
    "secret_access_key": "wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY",
    "session_token": None,
    "signing_region": "us-east-1",
    "signing_name": "service",
}


def _make_request(method: str, url: str, headers: dict[str, str]) -> Request:
    """Build a Request and strip headers Request adds by default that the
    AWS test suite does not include (Accept, User-Agent, Accept-Encoding).
    """
    req = Request(URL(url), method, headers=headers)
    for h in ("accept", "user-agent", "accept-encoding"):
        if h in req.headers:
            del req.headers[h]
    return req


def test_get_vanilla():
    """aws-sig-v4-test-suite/get-vanilla."""
    req = _make_request(
        "GET",
        "https://example.amazonaws.com/",
        {"Host": "example.amazonaws.com", "X-Amz-Date": "20150830T123600Z"},
    )
    signed = sign_sigv4(req, _TEST_SUITE_CTX, b"")
    assert signed.headers["Authorization"] == (
        "AWS4-HMAC-SHA256 "
        "Credential=AKIDEXAMPLE/20150830/us-east-1/service/aws4_request,"
        "SignedHeaders=host;x-amz-date,"
        "Signature=5fa00fa31553b73ebf1942676e86291e8372ff2a2260956d9b8aae1d763fbf31"
    )


def test_get_vanilla_query():
    """aws-sig-v4-test-suite/get-vanilla-query."""
    req = _make_request(
        "GET",
        "https://example.amazonaws.com/?Param1=value1",
        {"Host": "example.amazonaws.com", "X-Amz-Date": "20150830T123600Z"},
    )
    signed = sign_sigv4(req, _TEST_SUITE_CTX, b"")
    assert signed.headers["Authorization"] == (
        "AWS4-HMAC-SHA256 "
        "Credential=AKIDEXAMPLE/20150830/us-east-1/service/aws4_request,"
        "SignedHeaders=host;x-amz-date,"
        "Signature=a67d582fa61cc504c4bae71f336f98b97f1ea3c7a6bfe1b6e45aec72011b9aeb"
    )


def test_get_vanilla_query_order_key():
    """aws-sig-v4-test-suite/get-vanilla-query-order-key.

    Two params with the same prefix but different values; canonical order
    is alphabetical by encoded key.
    """
    req = _make_request(
        "GET",
        "https://example.amazonaws.com/?Param2=value2&Param1=value1",
        {"Host": "example.amazonaws.com", "X-Amz-Date": "20150830T123600Z"},
    )
    signed = sign_sigv4(req, _TEST_SUITE_CTX, b"")
    assert signed.headers["Authorization"] == (
        "AWS4-HMAC-SHA256 "
        "Credential=AKIDEXAMPLE/20150830/us-east-1/service/aws4_request,"
        "SignedHeaders=host;x-amz-date,"
        "Signature=b97d918cfa904a5beff61c982a1b6f458b799221646efd99d3219ec94cdf2500"
    )


def test_post_vanilla():
    """aws-sig-v4-test-suite/post-vanilla."""
    req = _make_request(
        "POST",
        "https://example.amazonaws.com/",
        {"Host": "example.amazonaws.com", "X-Amz-Date": "20150830T123600Z"},
    )
    signed = sign_sigv4(req, _TEST_SUITE_CTX, b"")
    assert signed.headers["Authorization"] == (
        "AWS4-HMAC-SHA256 "
        "Credential=AKIDEXAMPLE/20150830/us-east-1/service/aws4_request,"
        "SignedHeaders=host;x-amz-date,"
        "Signature=5da7c1a2acd57cee7505fc6676e4e544621c30862966e37dddb68e92efbe5d6b"
    )


# ---------------------------------------------------------------------------
# S3 examples from the AWS docs page
# ---------------------------------------------------------------------------


_S3_DOCS_CTX: SigV4AuthContext = {
    "type": "sig_v4",
    "access_key_id": "AKIAIOSFODNN7EXAMPLE",
    "secret_access_key": "wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY",
    "session_token": None,
    "signing_region": "us-east-1",
    "signing_name": "s3",
}


def test_s3_get_object_example():
    """``reference_sigv-create-signed-request`` — GET test.txt with Range."""
    req = _make_request(
        "GET",
        "https://examplebucket.s3.amazonaws.com/test.txt",
        {
            "Host": "examplebucket.s3.amazonaws.com",
            "Range": "bytes=0-9",
            "X-Amz-Date": "20130524T000000Z",
        },
    )
    signed = sign_sigv4(req, _S3_DOCS_CTX, b"")

    # Auto-injected payload hash for an empty body.
    assert signed.headers["X-Amz-Content-SHA256"] == (
        "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    )
    assert signed.headers["Authorization"] == (
        "AWS4-HMAC-SHA256 "
        "Credential=AKIAIOSFODNN7EXAMPLE/20130524/us-east-1/s3/aws4_request,"
        "SignedHeaders=host;range;x-amz-content-sha256;x-amz-date,"
        "Signature=67fe34c8530db585abddc51067328adfedb6e42487d2566dc7d927d6e2722900"
    )


# ---------------------------------------------------------------------------
# Behavioral tests
# ---------------------------------------------------------------------------


def test_session_token_added_and_signed():
    ctx: SigV4AuthContext = {**_TEST_SUITE_CTX, "session_token": "TOKEN123"}
    req = _make_request(
        "GET",
        "https://example.amazonaws.com/",
        {"Host": "example.amazonaws.com", "X-Amz-Date": "20150830T123600Z"},
    )
    signed = sign_sigv4(req, ctx, b"")
    assert signed.headers["X-Amz-Security-Token"] == "TOKEN123"
    # x-amz-security-token must appear in the signed-headers list.
    assert "x-amz-security-token" in signed.headers["Authorization"]


def test_s3_sets_payload_hash_for_body():
    req = _make_request(
        "PUT",
        "https://examplebucket.s3.amazonaws.com/key",
        {"Host": "examplebucket.s3.amazonaws.com", "X-Amz-Date": "20130524T000000Z"},
    )
    body = b"hello"
    signed = sign_sigv4(req, _S3_DOCS_CTX, body)
    # sha256("hello")
    assert signed.headers["X-Amz-Content-SHA256"] == (
        "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
    )


def test_non_s3_does_not_set_payload_hash_header():
    ctx: SigV4AuthContext = {**_TEST_SUITE_CTX, "signing_name": "iam"}
    req = _make_request(
        "GET",
        "https://iam.amazonaws.com/",
        {"Host": "iam.amazonaws.com", "X-Amz-Date": "20150830T123600Z"},
    )
    signed = sign_sigv4(req, ctx, b"")
    # IAM/STS/etc. signs the payload hash into the canonical request but does
    # not transmit an X-Amz-Content-SHA256 header.
    assert "X-Amz-Content-SHA256" not in signed.headers


def test_amz_date_autopopulated_when_missing():
    req = _make_request(
        "GET",
        "https://example.amazonaws.com/",
        {"Host": "example.amazonaws.com"},
    )
    signed = sign_sigv4(req, _TEST_SUITE_CTX, b"")
    amz_date = signed.headers["X-Amz-Date"]
    # Format: YYYYMMDDTHHMMSSZ
    assert len(amz_date) == 16
    assert amz_date.endswith("Z")
    assert amz_date[8] == "T"


def test_authorization_header_format():
    req = _make_request(
        "GET",
        "https://example.amazonaws.com/",
        {"Host": "example.amazonaws.com", "X-Amz-Date": "20150830T123600Z"},
    )
    signed = sign_sigv4(req, _TEST_SUITE_CTX, b"")
    auth = signed.headers["Authorization"]
    assert auth.startswith("AWS4-HMAC-SHA256 ")
    # Spec: comma-separated, no required whitespace between parts.
    parts = auth[len("AWS4-HMAC-SHA256 ") :].split(",")
    assert len(parts) == 3
    assert parts[0].startswith("Credential=")
    assert parts[1].startswith("SignedHeaders=")
    assert parts[2].startswith("Signature=")
    # 64 hex chars (SHA-256).
    sig = parts[2].removeprefix("Signature=")
    assert len(sig) == 64
    assert all(c in "0123456789abcdef" for c in sig)


def test_canonical_request_structure():
    """Round-trip a known canonical request through ``_build_canonical_request``."""
    headers = Headers(
        {
            "Host": "example.amazonaws.com",
            "X-Amz-Date": "20150830T123600Z",
        }
    )
    cr, signed = _build_canonical_request(
        method="GET",
        path="/",
        query="",
        headers=headers,
        payload_hash="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        service="service",
    )
    assert signed == "host;x-amz-date"
    assert cr == (
        "GET\n"
        "/\n"
        "\n"
        "host:example.amazonaws.com\n"
        "x-amz-date:20150830T123600Z\n"
        "\n"
        "host;x-amz-date\n"
        "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    )


def test_async_body_rejected(monkeypatch):
    """``sign_sigv4`` itself takes ``bytes``; the middleware enforces the
    no-async-stream rule. Smoke-test it via AuthMiddleware directly."""
    from aws_sdk_cost_explorer._auth._zapros_handler import AuthMiddleware

    async def _agen():  # pragma: no cover - never awaited
        yield b""

    class _Sink:
        def handle(self, request):  # pragma: no cover
            raise AssertionError("should not be reached")

    mw = AuthMiddleware(_Sink())
    req = Request(
        URL("https://example.amazonaws.com/"),
        "PUT",
        headers={"Host": "example.amazonaws.com"},
        body=_agen(),
        context={"smithy_auth": dict(_TEST_SUITE_CTX)},
    )
    with pytest.raises(Exception):
        mw.handle(req)
