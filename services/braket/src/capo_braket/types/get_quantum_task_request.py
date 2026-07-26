"""Generated from Smithy shape ``com.amazonaws.braket#GetQuantumTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_braket.types.quantum_task_additional_attribute_names_list
    import capo_braket.types.quantum_task_arn


class GetQuantumTaskRequest(TypedDict, closed=True):
    quantum_task_arn: "capo_braket.types.quantum_task_arn.QuantumTaskArn"
    """<p>The ARN of the quantum task to retrieve.</p>"""
    additional_attribute_names: NotRequired[
        "capo_braket.types.quantum_task_additional_attribute_names_list.QuantumTaskAdditionalAttributeNamesList"
    ]
    """<p>A list of attributes to return additional information for. Only the QueueInfo additional attribute name is currently supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQuantumTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetQuantumTaskRequest:
    out: GetQuantumTaskRequest = {}  # type: ignore[typeddict-item]
    return out
