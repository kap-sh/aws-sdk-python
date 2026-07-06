"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetails(TypedDict, closed=True):
    code: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The status code. </p>"""
    message: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The status message. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetails,
) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetails:
    out: AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetails = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
