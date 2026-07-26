"""Generated from Smithy shape ``com.amazonaws.controltower#ControlOperations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controltower.types.control_operation_summary

ControlOperations: TypeAlias = list[
    "capo_controltower.types.control_operation_summary.ControlOperationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlOperations) -> list:
    import capo_controltower.types.control_operation_summary

    out: list = []
    for item in value:
        out.append(
            capo_controltower.types.control_operation_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ControlOperations:
    import capo_controltower.types.control_operation_summary

    out: ControlOperations = []
    for item in data:
        out.append(
            capo_controltower.types.control_operation_summary.deserialize_json(item)
        )
    return out
