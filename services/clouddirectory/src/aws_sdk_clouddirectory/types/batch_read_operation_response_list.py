"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchReadOperationResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.batch_read_operation_response

BatchReadOperationResponseList: TypeAlias = list[
    "aws_sdk_clouddirectory.types.batch_read_operation_response.BatchReadOperationResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchReadOperationResponseList) -> list:
    import aws_sdk_clouddirectory.types.batch_read_operation_response

    out: list = []
    for item in value:
        out.append(
            aws_sdk_clouddirectory.types.batch_read_operation_response.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchReadOperationResponseList:
    import aws_sdk_clouddirectory.types.batch_read_operation_response

    out: BatchReadOperationResponseList = []
    for item in data:
        out.append(
            aws_sdk_clouddirectory.types.batch_read_operation_response.deserialize_json(
                item
            )
        )
    return out
