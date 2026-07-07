"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeMaintenanceWindowExecutionTaskInvocationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.maintenance_window_execution_id
    import aws_sdk_ssm.types.maintenance_window_execution_task_id
    import aws_sdk_ssm.types.maintenance_window_filter_list
    import aws_sdk_ssm.types.maintenance_window_max_results
    import aws_sdk_ssm.types.next_token


class DescribeMaintenanceWindowExecutionTaskInvocationsRequest(TypedDict, closed=True):
    window_execution_id: (
        "aws_sdk_ssm.types.maintenance_window_execution_id.MaintenanceWindowExecutionId"
    )
    """<p>The ID of the maintenance window execution the task is part of.</p>"""
    task_id: "aws_sdk_ssm.types.maintenance_window_execution_task_id.MaintenanceWindowExecutionTaskId"
    """<p>The ID of the specific task in the maintenance window task that should be retrieved.</p>"""
    filters: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_filter_list.MaintenanceWindowFilterList"
    ]
    """<p>Optional filters used to scope down the returned task invocations. The supported filter key is <code>STATUS</code> with the corresponding values <code>PENDING</code>, <code>IN_PROGRESS</code>, <code>SUCCESS</code>, <code>FAILED</code>, <code>TIMED_OUT</code>, <code>CANCELLING</code>, and <code>CANCELLED</code>.</p>"""
    max_results: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_max_results.MaintenanceWindowMaxResults"
    ]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeMaintenanceWindowExecutionTaskInvocationsRequest,
) -> dict:
    out: dict = {}
    out["WindowExecutionId"] = value["window_execution_id"]
    out["TaskId"] = value["task_id"]
    if "filters" in value:
        import aws_sdk_ssm.types.maintenance_window_filter_list

        out["Filters"] = (
            aws_sdk_ssm.types.maintenance_window_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeMaintenanceWindowExecutionTaskInvocationsRequest:
    out: DescribeMaintenanceWindowExecutionTaskInvocationsRequest = {}  # type: ignore[typeddict-item]
    if "WindowExecutionId" in data:
        out["window_execution_id"] = data["WindowExecutionId"]
    else:
        raise DeserializationError(
            "DescribeMaintenanceWindowExecutionTaskInvocationsRequest.window_execution_id required"
        )
    if "TaskId" in data:
        out["task_id"] = data["TaskId"]
    else:
        raise DeserializationError(
            "DescribeMaintenanceWindowExecutionTaskInvocationsRequest.task_id required"
        )
    if "Filters" in data:
        import aws_sdk_ssm.types.maintenance_window_filter_list

        out["filters"] = (
            aws_sdk_ssm.types.maintenance_window_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
