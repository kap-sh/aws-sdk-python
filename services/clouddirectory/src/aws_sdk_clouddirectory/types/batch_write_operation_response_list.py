"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchWriteOperationResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.batch_write_operation_response

BatchWriteOperationResponseList: TypeAlias = list[
    "aws_sdk_clouddirectory.types.batch_write_operation_response.BatchWriteOperationResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchWriteOperationResponseList) -> list:
    import aws_sdk_clouddirectory.types.batch_write_operation_response

    out: list = []
    for item in value:
        out.append(
            aws_sdk_clouddirectory.types.batch_write_operation_response.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchWriteOperationResponseList:
    import aws_sdk_clouddirectory.types.batch_write_operation_response

    out: BatchWriteOperationResponseList = []
    for item in data:
        out.append(
            aws_sdk_clouddirectory.types.batch_write_operation_response.deserialize_json(
                item
            )
        )
    return out
