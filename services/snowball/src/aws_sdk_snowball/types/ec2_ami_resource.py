"""Generated from Smithy shape ``com.amazonaws.snowball#Ec2AmiResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_snowball.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_snowball.types.ami_id
    import aws_sdk_snowball.types.string


class Ec2AmiResource(TypedDict, closed=True):
    ami_id: "aws_sdk_snowball.types.ami_id.AmiId"
    """<p>The ID of the AMI in Amazon EC2.</p>"""
    snowball_ami_id: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>The ID of the AMI on the Snow device.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Ec2AmiResource) -> dict:
    out: dict = {}
    out["AmiId"] = value["ami_id"]
    if "snowball_ami_id" in value:
        out["SnowballAmiId"] = value["snowball_ami_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Ec2AmiResource:
    out: Ec2AmiResource = {}  # type: ignore[typeddict-item]
    if "AmiId" in data:
        out["ami_id"] = data["AmiId"]
    else:
        raise DeserializationError("Ec2AmiResource.ami_id required")
    if "SnowballAmiId" in data:
        out["snowball_ami_id"] = data["SnowballAmiId"]
    return out
