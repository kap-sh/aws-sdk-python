"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3AccessPointVpcConfigurationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsS3AccessPointVpcConfigurationDetails(TypedDict):
    vpc_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> If this field is specified, this access point will only allow connections from the specified VPC ID. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3AccessPointVpcConfigurationDetails) -> dict:
    out: dict = {}
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    return out


def deserialize_json(data: dict) -> AwsS3AccessPointVpcConfigurationDetails:
    out: AwsS3AccessPointVpcConfigurationDetails = {}  # type: ignore[typeddict-item]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    return out
