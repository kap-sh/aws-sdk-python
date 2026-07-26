"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeMaintenanceWindowExecutionTasksResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_execution_task_identity_list
    import capo_ssm.types.next_token


class DescribeMaintenanceWindowExecutionTasksResult(TypedDict, closed=True):
    window_execution_task_identities: NotRequired[
        "capo_ssm.types.maintenance_window_execution_task_identity_list.MaintenanceWindowExecutionTaskIdentityList"
    ]
    """<p>Information about the task executions.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeMaintenanceWindowExecutionTasksResult,
) -> dict:
    out: dict = {}
    if "window_execution_task_identities" in value:
        import capo_ssm.types.maintenance_window_execution_task_identity_list

        out["WindowExecutionTaskIdentities"] = (
            capo_ssm.types.maintenance_window_execution_task_identity_list.serialize_aws_json_1_1(
                value["window_execution_task_identities"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeMaintenanceWindowExecutionTasksResult:
    out: DescribeMaintenanceWindowExecutionTasksResult = {}  # type: ignore[typeddict-item]
    if "WindowExecutionTaskIdentities" in data:
        import capo_ssm.types.maintenance_window_execution_task_identity_list

        out["window_execution_task_identities"] = (
            capo_ssm.types.maintenance_window_execution_task_identity_list.deserialize_aws_json_1_1(
                data["WindowExecutionTaskIdentities"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
