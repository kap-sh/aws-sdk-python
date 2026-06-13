"""Generated from Smithy shape ``com.amazonaws.braket#QuantumTaskSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_braket.types.quantum_task_summary

QuantumTaskSummaryList: TypeAlias = list[
    "aws_sdk_braket.types.quantum_task_summary.QuantumTaskSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuantumTaskSummaryList) -> list:
    import aws_sdk_braket.types.quantum_task_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_braket.types.quantum_task_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> QuantumTaskSummaryList:
    import aws_sdk_braket.types.quantum_task_summary

    out: QuantumTaskSummaryList = []
    for item in data:
        out.append(aws_sdk_braket.types.quantum_task_summary.deserialize_json(item))
    return out
