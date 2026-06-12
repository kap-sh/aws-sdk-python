"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeEC2InstanceLimitsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.ec2_instance_limit_list


class DescribeEC2InstanceLimitsOutput(TypedDict):
    ec2_instance_limits: NotRequired[
        "aws_sdk_gamelift.types.ec2_instance_limit_list.EC2InstanceLimitList"
    ]
    """<p>The maximum number of instances for the specified instance type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEC2InstanceLimitsOutput) -> dict:
    out: dict = {}
    if "ec2_instance_limits" in value:
        import aws_sdk_gamelift.types.ec2_instance_limit_list

        out["EC2InstanceLimits"] = (
            aws_sdk_gamelift.types.ec2_instance_limit_list.serialize_aws_json_1_1(
                value["ec2_instance_limits"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEC2InstanceLimitsOutput:
    out: DescribeEC2InstanceLimitsOutput = {}  # type: ignore[typeddict-item]
    if "EC2InstanceLimits" in data:
        import aws_sdk_gamelift.types.ec2_instance_limit_list

        out["ec2_instance_limits"] = (
            aws_sdk_gamelift.types.ec2_instance_limit_list.deserialize_aws_json_1_1(
                data["EC2InstanceLimits"]
            )
        )
    return out
