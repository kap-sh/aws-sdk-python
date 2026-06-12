"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2VpcPeeringConnectionStatusDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2VpcPeeringConnectionStatusDetails(TypedDict):
    code: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The status of the VPC peering connection. </p>"""
    message: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A message that provides more information about the status, if applicable. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2VpcPeeringConnectionStatusDetails) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AwsEc2VpcPeeringConnectionStatusDetails:
    out: AwsEc2VpcPeeringConnectionStatusDetails = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
