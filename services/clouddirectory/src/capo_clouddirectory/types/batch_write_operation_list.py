"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchWriteOperationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_clouddirectory.types.batch_write_operation

BatchWriteOperationList: TypeAlias = list[
    "capo_clouddirectory.types.batch_write_operation.BatchWriteOperation"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchWriteOperationList) -> list:
    import capo_clouddirectory.types.batch_write_operation

    out: list = []
    for item in value:
        out.append(capo_clouddirectory.types.batch_write_operation.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchWriteOperationList:
    import capo_clouddirectory.types.batch_write_operation

    out: BatchWriteOperationList = []
    for item in data:
        out.append(
            capo_clouddirectory.types.batch_write_operation.deserialize_json(item)
        )
    return out
