"""Generated from Smithy shape ``com.amazonaws.controltower#ControlOperationStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controltower.types.control_operation_status

ControlOperationStatuses: TypeAlias = list[
    "capo_controltower.types.control_operation_status.ControlOperationStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlOperationStatuses) -> list:
    import capo_controltower.types.control_operation_status

    out: list = []
    for item in value:
        out.append(
            capo_controltower.types.control_operation_status.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ControlOperationStatuses:
    import capo_controltower.types.control_operation_status

    out: ControlOperationStatuses = []
    for item in data:
        out.append(
            capo_controltower.types.control_operation_status.deserialize_json(item)
        )
    return out
