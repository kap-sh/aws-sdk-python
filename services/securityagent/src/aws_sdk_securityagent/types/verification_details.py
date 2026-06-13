"""Generated from Smithy shape ``com.amazonaws.securityagent#VerificationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.dns_verification
    import aws_sdk_securityagent.types.domain_verification_method
    import aws_sdk_securityagent.types.http_verification


class VerificationDetails(TypedDict):
    method: NotRequired[
        "aws_sdk_securityagent.types.domain_verification_method.DomainVerificationMethod"
    ]
    """<p>The verification method used for the target domain.</p>"""
    dns_txt: NotRequired["aws_sdk_securityagent.types.dns_verification.DnsVerification"]
    """<p>The DNS TXT verification details.</p>"""
    http_route: NotRequired[
        "aws_sdk_securityagent.types.http_verification.HttpVerification"
    ]
    """<p>The HTTP route verification details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VerificationDetails) -> dict:
    out: dict = {}
    if "method" in value:
        import aws_sdk_securityagent.types.domain_verification_method

        out["method"] = (
            aws_sdk_securityagent.types.domain_verification_method.serialize_json(
                value["method"]
            )
        )
    if "dns_txt" in value:
        import aws_sdk_securityagent.types.dns_verification

        out["dnsTxt"] = aws_sdk_securityagent.types.dns_verification.serialize_json(
            value["dns_txt"]
        )
    if "http_route" in value:
        import aws_sdk_securityagent.types.http_verification

        out["httpRoute"] = aws_sdk_securityagent.types.http_verification.serialize_json(
            value["http_route"]
        )
    return out


def deserialize_json(data: dict) -> VerificationDetails:
    out: VerificationDetails = {}  # type: ignore[typeddict-item]
    if "method" in data:
        import aws_sdk_securityagent.types.domain_verification_method

        out["method"] = (
            aws_sdk_securityagent.types.domain_verification_method.deserialize_json(
                data["method"]
            )
        )
    if "dnsTxt" in data:
        import aws_sdk_securityagent.types.dns_verification

        out["dns_txt"] = aws_sdk_securityagent.types.dns_verification.deserialize_json(
            data["dnsTxt"]
        )
    if "httpRoute" in data:
        import aws_sdk_securityagent.types.http_verification

        out["http_route"] = (
            aws_sdk_securityagent.types.http_verification.deserialize_json(
                data["httpRoute"]
            )
        )
    return out
