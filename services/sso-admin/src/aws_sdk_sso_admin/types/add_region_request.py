"""Generated from Smithy shape ``com.amazonaws.ssoadmin#AddRegionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.instance_arn
    import aws_sdk_sso_admin.types.region_name


class AddRegionRequest(TypedDict, closed=True):
    instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn"
    """<p>The Amazon Resource Name (ARN) of the IAM Identity Center instance to replicate to the target Region.</p>"""
    region_name: "aws_sdk_sso_admin.types.region_name.RegionName"
    """<p>The name of the Amazon Web Services Region to add to the IAM Identity Center instance. The Region name must be 1-32 characters long and follow the pattern of Amazon Web Services Region names (for example, us-east-1).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddRegionRequest) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    out["RegionName"] = value["region_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AddRegionRequest:
    out: AddRegionRequest = {}  # type: ignore[typeddict-item]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError("AddRegionRequest.instance_arn required")
    if "RegionName" in data:
        out["region_name"] = data["RegionName"]
    else:
        raise DeserializationError("AddRegionRequest.region_name required")
    return out
