"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeMaintenanceWindowExecutionTaskInvocationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.maintenance_window_execution_task_invocation_identity_list
    import aws_sdk_ssm.types.next_token


class DescribeMaintenanceWindowExecutionTaskInvocationsResult(TypedDict, closed=True):
    window_execution_task_invocation_identities: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_execution_task_invocation_identity_list.MaintenanceWindowExecutionTaskInvocationIdentityList"
    ]
    """<p>Information about the task invocation results per invocation.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeMaintenanceWindowExecutionTaskInvocationsResult,
) -> dict:
    out: dict = {}
    if "window_execution_task_invocation_identities" in value:
        import aws_sdk_ssm.types.maintenance_window_execution_task_invocation_identity_list

        out["WindowExecutionTaskInvocationIdentities"] = (
            aws_sdk_ssm.types.maintenance_window_execution_task_invocation_identity_list.serialize_aws_json_1_1(
                value["window_execution_task_invocation_identities"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeMaintenanceWindowExecutionTaskInvocationsResult:
    out: DescribeMaintenanceWindowExecutionTaskInvocationsResult = {}  # type: ignore[typeddict-item]
    if "WindowExecutionTaskInvocationIdentities" in data:
        import aws_sdk_ssm.types.maintenance_window_execution_task_invocation_identity_list

        out["window_execution_task_invocation_identities"] = (
            aws_sdk_ssm.types.maintenance_window_execution_task_invocation_identity_list.deserialize_aws_json_1_1(
                data["WindowExecutionTaskInvocationIdentities"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
