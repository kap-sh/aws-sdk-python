"""Generated from Smithy shape ``com.amazonaws.controltower#ControlOperationStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_controltower.types.control_operation_status

ControlOperationStatuses: TypeAlias = list[
    "aws_sdk_controltower.types.control_operation_status.ControlOperationStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlOperationStatuses) -> list:
    import aws_sdk_controltower.types.control_operation_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_controltower.types.control_operation_status.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ControlOperationStatuses:
    import aws_sdk_controltower.types.control_operation_status

    out: ControlOperationStatuses = []
    for item in data:
        out.append(
            aws_sdk_controltower.types.control_operation_status.deserialize_json(item)
        )
    return out
