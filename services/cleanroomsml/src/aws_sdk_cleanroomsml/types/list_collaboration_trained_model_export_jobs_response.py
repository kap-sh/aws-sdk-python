"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListCollaborationTrainedModelExportJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.collaboration_trained_model_export_job_list
    import aws_sdk_cleanroomsml.types.next_token


class ListCollaborationTrainedModelExportJobsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value used to access the next page of results.</p>"""
    collaboration_trained_model_export_jobs: "aws_sdk_cleanroomsml.types.collaboration_trained_model_export_job_list.CollaborationTrainedModelExportJobList"
    """<p>The exports jobs that exist for the requested trained model in the requested collaboration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollaborationTrainedModelExportJobsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_cleanroomsml.types.collaboration_trained_model_export_job_list

    out["collaborationTrainedModelExportJobs"] = (
        aws_sdk_cleanroomsml.types.collaboration_trained_model_export_job_list.serialize_json(
            value["collaboration_trained_model_export_jobs"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListCollaborationTrainedModelExportJobsResponse:
    out: ListCollaborationTrainedModelExportJobsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "collaborationTrainedModelExportJobs" in data:
        import aws_sdk_cleanroomsml.types.collaboration_trained_model_export_job_list

        out["collaboration_trained_model_export_jobs"] = (
            aws_sdk_cleanroomsml.types.collaboration_trained_model_export_job_list.deserialize_json(
                data["collaborationTrainedModelExportJobs"]
            )
        )
    else:
        raise DeserializationError(
            "ListCollaborationTrainedModelExportJobsResponse.collaboration_trained_model_export_jobs required"
        )
    return out
