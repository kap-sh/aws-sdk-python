"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfBatchSuccessfulResultModel``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.batch_successful_result_model

__listOfBatchSuccessfulResultModel: TypeAlias = list[
    "aws_sdk_medialive.types.batch_successful_result_model.BatchSuccessfulResultModel"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfBatchSuccessfulResultModel) -> list:
    import aws_sdk_medialive.types.batch_successful_result_model

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medialive.types.batch_successful_result_model.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfBatchSuccessfulResultModel:
    import aws_sdk_medialive.types.batch_successful_result_model

    out: __listOfBatchSuccessfulResultModel = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.batch_successful_result_model.deserialize_json(item)
        )
    return out
