"""Generated from Smithy shape ``com.amazonaws.braket#CancelQuantumTaskResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_braket.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_braket.types.cancellation_status
    import aws_sdk_braket.types.quantum_task_arn

class CancelQuantumTaskResponse(TypedDict):
    quantum_task_arn: "aws_sdk_braket.types.quantum_task_arn.QuantumTaskArn"
    """<p>The ARN of the quantum task.</p>"""
    cancellation_status: "aws_sdk_braket.types.cancellation_status.CancellationStatus"
    """<p>The status of the quantum task.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CancelQuantumTaskResponse) -> dict:
    out: dict = {}
    out["quantumTaskArn"] = value["quantum_task_arn"]
    out["cancellationStatus"] = value["cancellation_status"]
    return out


def deserialize_json(data: dict) -> CancelQuantumTaskResponse:
    out: CancelQuantumTaskResponse = {}  # type: ignore[typeddict-item]
    if "quantumTaskArn" in data:
        out["quantum_task_arn"] = data["quantumTaskArn"]
    else:
        raise DeserializationError("CancelQuantumTaskResponse.quantum_task_arn required")
    if "cancellationStatus" in data:
        out["cancellation_status"] = data["cancellationStatus"]
    else:
        raise DeserializationError("CancelQuantumTaskResponse.cancellation_status required")
    return out