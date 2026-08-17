"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeMaintenanceWindowExecutionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_execution_list
    import capo_ssm.types.next_token


class DescribeMaintenanceWindowExecutionsResult(TypedDict, closed=True):
    window_executions: NotRequired[
        "capo_ssm.types.maintenance_window_execution_list.MaintenanceWindowExecutionList"
    ]
    """<p>Information about the maintenance window executions.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMaintenanceWindowExecutionsResult) -> dict:
    out: dict = {}
    if "window_executions" in value:
        import capo_ssm.types.maintenance_window_execution_list

        out["WindowExecutions"] = (
            capo_ssm.types.maintenance_window_execution_list.serialize_aws_json_1_1(
                value["window_executions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMaintenanceWindowExecutionsResult:
    out: DescribeMaintenanceWindowExecutionsResult = {}  # type: ignore[typeddict-item]
    if data.get("WindowExecutions") is not None:
        import capo_ssm.types.maintenance_window_execution_list

        out["window_executions"] = (
            capo_ssm.types.maintenance_window_execution_list.deserialize_aws_json_1_1(
                data["WindowExecutions"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
