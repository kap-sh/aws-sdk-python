"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CollaborationTrainedModelInferenceJobList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanroomsml.types.collaboration_trained_model_inference_job_summary

CollaborationTrainedModelInferenceJobList: TypeAlias = list[
    "capo_cleanroomsml.types.collaboration_trained_model_inference_job_summary.CollaborationTrainedModelInferenceJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationTrainedModelInferenceJobList) -> list:
    import capo_cleanroomsml.types.collaboration_trained_model_inference_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_cleanroomsml.types.collaboration_trained_model_inference_job_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CollaborationTrainedModelInferenceJobList:
    import capo_cleanroomsml.types.collaboration_trained_model_inference_job_summary

    out: CollaborationTrainedModelInferenceJobList = []
    for item in data:
        out.append(
            capo_cleanroomsml.types.collaboration_trained_model_inference_job_summary.deserialize_json(
                item
            )
        )
    return out
