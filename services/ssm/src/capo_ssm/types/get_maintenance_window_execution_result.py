"""Generated from Smithy shape ``com.amazonaws.ssm#GetMaintenanceWindowExecutionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.date_time
    import capo_ssm.types.maintenance_window_execution_id
    import capo_ssm.types.maintenance_window_execution_status
    import capo_ssm.types.maintenance_window_execution_status_details
    import capo_ssm.types.maintenance_window_execution_task_id_list


class GetMaintenanceWindowExecutionResult(TypedDict, closed=True):
    window_execution_id: NotRequired[
        "capo_ssm.types.maintenance_window_execution_id.MaintenanceWindowExecutionId"
    ]
    """<p>The ID of the maintenance window execution.</p>"""
    task_ids: NotRequired[
        "capo_ssm.types.maintenance_window_execution_task_id_list.MaintenanceWindowExecutionTaskIdList"
    ]
    """<p>The ID of the task executions from the maintenance window execution.</p>"""
    status: NotRequired[
        "capo_ssm.types.maintenance_window_execution_status.MaintenanceWindowExecutionStatus"
    ]
    """<p>The status of the maintenance window execution.</p>"""
    status_details: NotRequired[
        "capo_ssm.types.maintenance_window_execution_status_details.MaintenanceWindowExecutionStatusDetails"
    ]
    """<p>The details explaining the status. Not available for all status values.</p>"""
    start_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time the maintenance window started running.</p>"""
    end_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time the maintenance window finished running.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMaintenanceWindowExecutionResult) -> dict:
    out: dict = {}
    if "window_execution_id" in value:
        out["WindowExecutionId"] = value["window_execution_id"]
    if "task_ids" in value:
        import capo_ssm.types.maintenance_window_execution_task_id_list

        out["TaskIds"] = (
            capo_ssm.types.maintenance_window_execution_task_id_list.serialize_aws_json_1_1(
                value["task_ids"]
            )
        )
    if "status" in value:
        import capo_ssm.types.maintenance_window_execution_status

        out["Status"] = (
            capo_ssm.types.maintenance_window_execution_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_details" in value:
        out["StatusDetails"] = value["status_details"]
    if "start_time" in value:
        import capo_ssm.types.date_time

        out["StartTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_ssm.types.date_time

        out["EndTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["end_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMaintenanceWindowExecutionResult:
    out: GetMaintenanceWindowExecutionResult = {}  # type: ignore[typeddict-item]
    if data.get("WindowExecutionId") is not None:
        out["window_execution_id"] = data["WindowExecutionId"]
    if data.get("TaskIds") is not None:
        import capo_ssm.types.maintenance_window_execution_task_id_list

        out["task_ids"] = (
            capo_ssm.types.maintenance_window_execution_task_id_list.deserialize_aws_json_1_1(
                data["TaskIds"]
            )
        )
    if data.get("Status") is not None:
        import capo_ssm.types.maintenance_window_execution_status

        out["status"] = (
            capo_ssm.types.maintenance_window_execution_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("StatusDetails") is not None:
        out["status_details"] = data["StatusDetails"]
    if data.get("StartTime") is not None:
        import capo_ssm.types.date_time

        out["start_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_ssm.types.date_time

        out["end_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    return out
