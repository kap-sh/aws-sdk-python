"""Generated from Smithy shape ``com.amazonaws.braket#QuantumTaskAdditionalAttributeNamesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_braket.types.quantum_task_additional_attribute_name

QuantumTaskAdditionalAttributeNamesList: TypeAlias = list[
    "aws_sdk_braket.types.quantum_task_additional_attribute_name.QuantumTaskAdditionalAttributeName"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuantumTaskAdditionalAttributeNamesList) -> list:
    return list(value)


def deserialize_json(data: list) -> QuantumTaskAdditionalAttributeNamesList:
    return list(data)
