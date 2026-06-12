"""Generated from Smithy shape ``com.amazonaws.controltower#ControlOperationTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_controltower.types.control_operation_type

ControlOperationTypes: TypeAlias = list[
    "aws_sdk_controltower.types.control_operation_type.ControlOperationType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlOperationTypes) -> list:
    import aws_sdk_controltower.types.control_operation_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_controltower.types.control_operation_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ControlOperationTypes:
    import aws_sdk_controltower.types.control_operation_type

    out: ControlOperationTypes = []
    for item in data:
        out.append(
            aws_sdk_controltower.types.control_operation_type.deserialize_json(item)
        )
    return out
