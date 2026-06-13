"""Generated from Smithy shape ``com.amazonaws.braket#SearchQuantumTasksFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_braket.types.search_quantum_tasks_filter

SearchQuantumTasksFilterList: TypeAlias = list[
    "aws_sdk_braket.types.search_quantum_tasks_filter.SearchQuantumTasksFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchQuantumTasksFilterList) -> list:
    import aws_sdk_braket.types.search_quantum_tasks_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_braket.types.search_quantum_tasks_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SearchQuantumTasksFilterList:
    import aws_sdk_braket.types.search_quantum_tasks_filter

    out: SearchQuantumTasksFilterList = []
    for item in data:
        out.append(
            aws_sdk_braket.types.search_quantum_tasks_filter.deserialize_json(item)
        )
    return out
