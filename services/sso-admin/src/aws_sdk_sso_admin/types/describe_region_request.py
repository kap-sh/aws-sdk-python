"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DescribeRegionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.instance_arn
    import aws_sdk_sso_admin.types.region_name


class DescribeRegionRequest(TypedDict):
    instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn"
    """<p>The Amazon Resource Name (ARN) of the IAM Identity Center instance.</p>"""
    region_name: "aws_sdk_sso_admin.types.region_name.RegionName"
    """<p>The name of the Amazon Web Services Region to retrieve information about. The Region name must be 1-32 characters long and follow the pattern of Amazon Web Services Region names (for example, us-east-1).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRegionRequest) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    out["RegionName"] = value["region_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRegionRequest:
    out: DescribeRegionRequest = {}  # type: ignore[typeddict-item]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError("DescribeRegionRequest.instance_arn required")
    if "RegionName" in data:
        out["region_name"] = data["RegionName"]
    else:
        raise DeserializationError("DescribeRegionRequest.region_name required")
    return out
