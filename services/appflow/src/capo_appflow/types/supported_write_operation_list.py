"""Generated from Smithy shape ``com.amazonaws.appflow#SupportedWriteOperationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appflow.types.write_operation_type

SupportedWriteOperationList: TypeAlias = list[
    "capo_appflow.types.write_operation_type.WriteOperationType"
]


# --- restJson1 ser/de ---
def serialize_json(value: SupportedWriteOperationList) -> list:
    import capo_appflow.types.write_operation_type

    out: list = []
    for item in value:
        out.append(capo_appflow.types.write_operation_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> SupportedWriteOperationList:
    import capo_appflow.types.write_operation_type

    out: SupportedWriteOperationList = []
    for item in data:
        out.append(capo_appflow.types.write_operation_type.deserialize_json(item))
    return out
