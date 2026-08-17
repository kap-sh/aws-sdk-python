"""Generated from Smithy shape ``com.amazonaws.ssm#CancelMaintenanceWindowExecutionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_execution_id


class CancelMaintenanceWindowExecutionResult(TypedDict, closed=True):
    window_execution_id: NotRequired[
        "capo_ssm.types.maintenance_window_execution_id.MaintenanceWindowExecutionId"
    ]
    """<p>The ID of the maintenance window execution that has been stopped.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelMaintenanceWindowExecutionResult) -> dict:
    out: dict = {}
    if "window_execution_id" in value:
        out["WindowExecutionId"] = value["window_execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelMaintenanceWindowExecutionResult:
    out: CancelMaintenanceWindowExecutionResult = {}  # type: ignore[typeddict-item]
    if data.get("WindowExecutionId") is not None:
        out["window_execution_id"] = data["WindowExecutionId"]
    return out
