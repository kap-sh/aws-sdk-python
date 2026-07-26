"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolNetworkOperationTaskDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_tnb.types.error_info
    import capo_tnb.types.string_map
    import capo_tnb.types.task_status


class GetSolNetworkOperationTaskDetails(TypedDict, closed=True):
    task_name: NotRequired["str"]
    """<p>Task name.</p>"""
    task_context: NotRequired["capo_tnb.types.string_map.StringMap"]
    """<p>Context for the network operation task.</p>"""
    task_error_details: NotRequired["capo_tnb.types.error_info.ErrorInfo"]
    """<p>Task error details.</p>"""
    task_status: NotRequired["capo_tnb.types.task_status.TaskStatus"]
    """<p>Task status.</p>"""
    task_start_time: NotRequired["datetime.datetime"]
    """<p>Task start time.</p>"""
    task_end_time: NotRequired["datetime.datetime"]
    """<p>Task end time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolNetworkOperationTaskDetails) -> dict:
    out: dict = {}
    if "task_name" in value:
        out["taskName"] = value["task_name"]
    if "task_context" in value:
        import capo_tnb.types.string_map

        out["taskContext"] = capo_tnb.types.string_map.serialize_json(
            value["task_context"]
        )
    if "task_error_details" in value:
        import capo_tnb.types.error_info

        out["taskErrorDetails"] = capo_tnb.types.error_info.serialize_json(
            value["task_error_details"]
        )
    if "task_status" in value:
        import capo_tnb.types.task_status

        out["taskStatus"] = capo_tnb.types.task_status.serialize_json(
            value["task_status"]
        )
    if "task_start_time" in value:
        import capo_tnb.types._prelude.timestamp

        out["taskStartTime"] = capo_tnb.types._prelude.timestamp.serialize_json(
            value["task_start_time"]
        )
    if "task_end_time" in value:
        import capo_tnb.types._prelude.timestamp

        out["taskEndTime"] = capo_tnb.types._prelude.timestamp.serialize_json(
            value["task_end_time"]
        )
    return out


def deserialize_json(data: dict) -> GetSolNetworkOperationTaskDetails:
    out: GetSolNetworkOperationTaskDetails = {}  # type: ignore[typeddict-item]
    if "taskName" in data:
        out["task_name"] = data["taskName"]
    if "taskContext" in data:
        import capo_tnb.types.string_map

        out["task_context"] = capo_tnb.types.string_map.deserialize_json(
            data["taskContext"]
        )
    if "taskErrorDetails" in data:
        import capo_tnb.types.error_info

        out["task_error_details"] = capo_tnb.types.error_info.deserialize_json(
            data["taskErrorDetails"]
        )
    if "taskStatus" in data:
        import capo_tnb.types.task_status

        out["task_status"] = capo_tnb.types.task_status.deserialize_json(
            data["taskStatus"]
        )
    if "taskStartTime" in data:
        import capo_tnb.types._prelude.timestamp

        out["task_start_time"] = capo_tnb.types._prelude.timestamp.deserialize_json(
            data["taskStartTime"]
        )
    if "taskEndTime" in data:
        import capo_tnb.types._prelude.timestamp

        out["task_end_time"] = capo_tnb.types._prelude.timestamp.deserialize_json(
            data["taskEndTime"]
        )
    return out
