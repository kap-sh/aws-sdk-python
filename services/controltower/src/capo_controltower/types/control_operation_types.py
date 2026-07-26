"""Generated from Smithy shape ``com.amazonaws.controltower#ControlOperationTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controltower.types.control_operation_type

ControlOperationTypes: TypeAlias = list[
    "capo_controltower.types.control_operation_type.ControlOperationType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlOperationTypes) -> list:
    import capo_controltower.types.control_operation_type

    out: list = []
    for item in value:
        out.append(capo_controltower.types.control_operation_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ControlOperationTypes:
    import capo_controltower.types.control_operation_type

    out: ControlOperationTypes = []
    for item in data:
        out.append(
            capo_controltower.types.control_operation_type.deserialize_json(item)
        )
    return out
