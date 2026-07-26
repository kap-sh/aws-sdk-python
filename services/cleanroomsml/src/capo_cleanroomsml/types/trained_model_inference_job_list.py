"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelInferenceJobList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanroomsml.types.trained_model_inference_job_summary

TrainedModelInferenceJobList: TypeAlias = list[
    "capo_cleanroomsml.types.trained_model_inference_job_summary.TrainedModelInferenceJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TrainedModelInferenceJobList) -> list:
    import capo_cleanroomsml.types.trained_model_inference_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_cleanroomsml.types.trained_model_inference_job_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TrainedModelInferenceJobList:
    import capo_cleanroomsml.types.trained_model_inference_job_summary

    out: TrainedModelInferenceJobList = []
    for item in data:
        out.append(
            capo_cleanroomsml.types.trained_model_inference_job_summary.deserialize_json(
                item
            )
        )
    return out
