"""Generated from Smithy shape ``com.amazonaws.acm#HttpRedirect``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_acm.types.string


class HttpRedirect(TypedDict):
    redirect_from: NotRequired["aws_sdk_acm.types.string.String"]
    """<p>The URL including the domain to be validated. The certificate authority sends <code>GET</code> requests here during validation.</p>"""
    redirect_to: NotRequired["aws_sdk_acm.types.string.String"]
    """<p>The URL hosting the validation token. <code>RedirectFrom</code> must return this content or redirect here.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HttpRedirect) -> dict:
    out: dict = {}
    if "redirect_from" in value:
        out["RedirectFrom"] = value["redirect_from"]
    if "redirect_to" in value:
        out["RedirectTo"] = value["redirect_to"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HttpRedirect:
    out: HttpRedirect = {}  # type: ignore[typeddict-item]
    if "RedirectFrom" in data:
        out["redirect_from"] = data["RedirectFrom"]
    if "RedirectTo" in data:
        out["redirect_to"] = data["RedirectTo"]
    return out
