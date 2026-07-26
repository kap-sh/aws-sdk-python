"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchReadOperationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_clouddirectory.types.batch_read_operation

BatchReadOperationList: TypeAlias = list[
    "capo_clouddirectory.types.batch_read_operation.BatchReadOperation"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchReadOperationList) -> list:
    import capo_clouddirectory.types.batch_read_operation

    out: list = []
    for item in value:
        out.append(capo_clouddirectory.types.batch_read_operation.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchReadOperationList:
    import capo_clouddirectory.types.batch_read_operation

    out: BatchReadOperationList = []
    for item in data:
        out.append(
            capo_clouddirectory.types.batch_read_operation.deserialize_json(item)
        )
    return out
