"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DescribeInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.instance_arn


class DescribeInstanceRequest(TypedDict, closed=True):
    instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn"
    """<p>The ARN of the instance of IAM Identity Center under which the operation will run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInstanceRequest) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeInstanceRequest:
    out: DescribeInstanceRequest = {}  # type: ignore[typeddict-item]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError("DescribeInstanceRequest.instance_arn required")
    return out
