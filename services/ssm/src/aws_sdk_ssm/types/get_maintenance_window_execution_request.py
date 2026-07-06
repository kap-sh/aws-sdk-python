"""Generated from Smithy shape ``com.amazonaws.ssm#GetMaintenanceWindowExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.maintenance_window_execution_id


class GetMaintenanceWindowExecutionRequest(TypedDict, closed=True):
    window_execution_id: (
        "aws_sdk_ssm.types.maintenance_window_execution_id.MaintenanceWindowExecutionId"
    )
    """<p>The ID of the maintenance window execution that includes the task.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMaintenanceWindowExecutionRequest) -> dict:
    out: dict = {}
    out["WindowExecutionId"] = value["window_execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMaintenanceWindowExecutionRequest:
    out: GetMaintenanceWindowExecutionRequest = {}  # type: ignore[typeddict-item]
    if "WindowExecutionId" in data:
        out["window_execution_id"] = data["WindowExecutionId"]
    else:
        raise DeserializationError(
            "GetMaintenanceWindowExecutionRequest.window_execution_id required"
        )
    return out
