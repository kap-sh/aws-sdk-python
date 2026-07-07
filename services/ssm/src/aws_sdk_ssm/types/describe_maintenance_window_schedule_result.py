"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeMaintenanceWindowScheduleResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.next_token
    import aws_sdk_ssm.types.scheduled_window_execution_list


class DescribeMaintenanceWindowScheduleResult(TypedDict, closed=True):
    scheduled_window_executions: NotRequired[
        "aws_sdk_ssm.types.scheduled_window_execution_list.ScheduledWindowExecutionList"
    ]
    """<p>Information about maintenance window executions scheduled for the specified time range.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You use this token in the next call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMaintenanceWindowScheduleResult) -> dict:
    out: dict = {}
    if "scheduled_window_executions" in value:
        import aws_sdk_ssm.types.scheduled_window_execution_list

        out["ScheduledWindowExecutions"] = (
            aws_sdk_ssm.types.scheduled_window_execution_list.serialize_aws_json_1_1(
                value["scheduled_window_executions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMaintenanceWindowScheduleResult:
    out: DescribeMaintenanceWindowScheduleResult = {}  # type: ignore[typeddict-item]
    if "ScheduledWindowExecutions" in data:
        import aws_sdk_ssm.types.scheduled_window_execution_list

        out["scheduled_window_executions"] = (
            aws_sdk_ssm.types.scheduled_window_execution_list.deserialize_aws_json_1_1(
                data["ScheduledWindowExecutions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
