"""Generated from Smithy shape ``com.amazonaws.ssm#GetMaintenanceWindowExecutionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.date_time
    import aws_sdk_ssm.types.maintenance_window_execution_id
    import aws_sdk_ssm.types.maintenance_window_execution_status
    import aws_sdk_ssm.types.maintenance_window_execution_status_details
    import aws_sdk_ssm.types.maintenance_window_execution_task_id_list


class GetMaintenanceWindowExecutionResult(TypedDict, closed=True):
    window_execution_id: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_execution_id.MaintenanceWindowExecutionId"
    ]
    """<p>The ID of the maintenance window execution.</p>"""
    task_ids: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_execution_task_id_list.MaintenanceWindowExecutionTaskIdList"
    ]
    """<p>The ID of the task executions from the maintenance window execution.</p>"""
    status: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_execution_status.MaintenanceWindowExecutionStatus"
    ]
    """<p>The status of the maintenance window execution.</p>"""
    status_details: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_execution_status_details.MaintenanceWindowExecutionStatusDetails"
    ]
    """<p>The details explaining the status. Not available for all status values.</p>"""
    start_time: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The time the maintenance window started running.</p>"""
    end_time: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The time the maintenance window finished running.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMaintenanceWindowExecutionResult) -> dict:
    out: dict = {}
    if "window_execution_id" in value:
        out["WindowExecutionId"] = value["window_execution_id"]
    if "task_ids" in value:
        import aws_sdk_ssm.types.maintenance_window_execution_task_id_list

        out["TaskIds"] = (
            aws_sdk_ssm.types.maintenance_window_execution_task_id_list.serialize_aws_json_1_1(
                value["task_ids"]
            )
        )
    if "status" in value:
        import aws_sdk_ssm.types.maintenance_window_execution_status

        out["Status"] = (
            aws_sdk_ssm.types.maintenance_window_execution_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_details" in value:
        out["StatusDetails"] = value["status_details"]
    if "start_time" in value:
        import aws_sdk_ssm.types.date_time

        out["StartTime"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_ssm.types.date_time

        out["EndTime"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["end_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMaintenanceWindowExecutionResult:
    out: GetMaintenanceWindowExecutionResult = {}  # type: ignore[typeddict-item]
    if "WindowExecutionId" in data:
        out["window_execution_id"] = data["WindowExecutionId"]
    if "TaskIds" in data:
        import aws_sdk_ssm.types.maintenance_window_execution_task_id_list

        out["task_ids"] = (
            aws_sdk_ssm.types.maintenance_window_execution_task_id_list.deserialize_aws_json_1_1(
                data["TaskIds"]
            )
        )
    if "Status" in data:
        import aws_sdk_ssm.types.maintenance_window_execution_status

        out["status"] = (
            aws_sdk_ssm.types.maintenance_window_execution_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusDetails" in data:
        out["status_details"] = data["StatusDetails"]
    if "StartTime" in data:
        import aws_sdk_ssm.types.date_time

        out["start_time"] = aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import aws_sdk_ssm.types.date_time

        out["end_time"] = aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    return out
