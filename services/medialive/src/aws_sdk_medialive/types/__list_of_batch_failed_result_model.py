"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfBatchFailedResultModel``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.batch_failed_result_model

__listOfBatchFailedResultModel: TypeAlias = list[
    "aws_sdk_medialive.types.batch_failed_result_model.BatchFailedResultModel"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfBatchFailedResultModel) -> list:
    import aws_sdk_medialive.types.batch_failed_result_model

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medialive.types.batch_failed_result_model.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfBatchFailedResultModel:
    import aws_sdk_medialive.types.batch_failed_result_model

    out: __listOfBatchFailedResultModel = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.batch_failed_result_model.deserialize_json(item)
        )
    return out
