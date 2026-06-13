"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CollaborationTrainedModelExportJobList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.collaboration_trained_model_export_job_summary

CollaborationTrainedModelExportJobList: TypeAlias = list[
    "aws_sdk_cleanroomsml.types.collaboration_trained_model_export_job_summary.CollaborationTrainedModelExportJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationTrainedModelExportJobList) -> list:
    import aws_sdk_cleanroomsml.types.collaboration_trained_model_export_job_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanroomsml.types.collaboration_trained_model_export_job_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CollaborationTrainedModelExportJobList:
    import aws_sdk_cleanroomsml.types.collaboration_trained_model_export_job_summary

    out: CollaborationTrainedModelExportJobList = []
    for item in data:
        out.append(
            aws_sdk_cleanroomsml.types.collaboration_trained_model_export_job_summary.deserialize_json(
                item
            )
        )
    return out
