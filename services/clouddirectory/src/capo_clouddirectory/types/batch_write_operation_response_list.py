"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchWriteOperationResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_clouddirectory.types.batch_write_operation_response

BatchWriteOperationResponseList: TypeAlias = list[
    "capo_clouddirectory.types.batch_write_operation_response.BatchWriteOperationResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchWriteOperationResponseList) -> list:
    import capo_clouddirectory.types.batch_write_operation_response

    out: list = []
    for item in value:
        out.append(
            capo_clouddirectory.types.batch_write_operation_response.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchWriteOperationResponseList:
    import capo_clouddirectory.types.batch_write_operation_response

    out: BatchWriteOperationResponseList = []
    for item in data:
        out.append(
            capo_clouddirectory.types.batch_write_operation_response.deserialize_json(
                item
            )
        )
    return out
