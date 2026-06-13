"""Generated from Smithy shape ``com.amazonaws.braket#CancelQuantumTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_braket.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_braket.types.quantum_task_arn
    import aws_sdk_braket.types.string64


class CancelQuantumTaskRequest(TypedDict):
    quantum_task_arn: "aws_sdk_braket.types.quantum_task_arn.QuantumTaskArn"
    """<p>The ARN of the quantum task to cancel.</p>"""
    client_token: "aws_sdk_braket.types.string64.String64"
    """<p>The client token associated with the cancellation request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelQuantumTaskRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CancelQuantumTaskRequest:
    out: CancelQuantumTaskRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("CancelQuantumTaskRequest.client_token required")
    return out
