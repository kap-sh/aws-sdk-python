"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchReadOperationResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_clouddirectory.types.batch_read_operation_response

BatchReadOperationResponseList: TypeAlias = list[
    "capo_clouddirectory.types.batch_read_operation_response.BatchReadOperationResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchReadOperationResponseList) -> list:
    import capo_clouddirectory.types.batch_read_operation_response

    out: list = []
    for item in value:
        out.append(
            capo_clouddirectory.types.batch_read_operation_response.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchReadOperationResponseList:
    import capo_clouddirectory.types.batch_read_operation_response

    out: BatchReadOperationResponseList = []
    for item in data:
        out.append(
            capo_clouddirectory.types.batch_read_operation_response.deserialize_json(
                item
            )
        )
    return out
