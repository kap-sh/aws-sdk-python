"""Generated from Smithy shape ``com.amazonaws.workmail#DescribeEmailMonitoringConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.log_group_arn
    import aws_sdk_workmail.types.role_arn


class DescribeEmailMonitoringConfigurationResponse(TypedDict):
    role_arn: NotRequired["aws_sdk_workmail.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM Role associated with the email monitoring configuration.</p>"""
    log_group_arn: NotRequired["aws_sdk_workmail.types.log_group_arn.LogGroupArn"]
    """<p>The Amazon Resource Name (ARN) of the CloudWatch Log group associated with the email monitoring configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEmailMonitoringConfigurationResponse) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "log_group_arn" in value:
        out["LogGroupArn"] = value["log_group_arn"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeEmailMonitoringConfigurationResponse:
    out: DescribeEmailMonitoringConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "LogGroupArn" in data:
        out["log_group_arn"] = data["LogGroupArn"]
    return out
