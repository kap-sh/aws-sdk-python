"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfBatchFailedResultModel``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.batch_failed_result_model

__listOfBatchFailedResultModel: TypeAlias = list[
    "capo_medialive.types.batch_failed_result_model.BatchFailedResultModel"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfBatchFailedResultModel) -> list:
    import capo_medialive.types.batch_failed_result_model

    out: list = []
    for item in value:
        out.append(capo_medialive.types.batch_failed_result_model.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfBatchFailedResultModel:
    import capo_medialive.types.batch_failed_result_model

    out: __listOfBatchFailedResultModel = []
    for item in data:
        out.append(
            capo_medialive.types.batch_failed_result_model.deserialize_json(item)
        )
    return out
