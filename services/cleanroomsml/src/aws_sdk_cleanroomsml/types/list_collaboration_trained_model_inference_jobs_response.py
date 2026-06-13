"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListCollaborationTrainedModelInferenceJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.collaboration_trained_model_inference_job_list
    import aws_sdk_cleanroomsml.types.next_token


class ListCollaborationTrainedModelInferenceJobsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value used to access the next page of results.</p>"""
    collaboration_trained_model_inference_jobs: "aws_sdk_cleanroomsml.types.collaboration_trained_model_inference_job_list.CollaborationTrainedModelInferenceJobList"
    """<p>The trained model inference jobs that you are interested in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollaborationTrainedModelInferenceJobsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_cleanroomsml.types.collaboration_trained_model_inference_job_list

    out["collaborationTrainedModelInferenceJobs"] = (
        aws_sdk_cleanroomsml.types.collaboration_trained_model_inference_job_list.serialize_json(
            value["collaboration_trained_model_inference_jobs"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListCollaborationTrainedModelInferenceJobsResponse:
    out: ListCollaborationTrainedModelInferenceJobsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "collaborationTrainedModelInferenceJobs" in data:
        import aws_sdk_cleanroomsml.types.collaboration_trained_model_inference_job_list

        out["collaboration_trained_model_inference_jobs"] = (
            aws_sdk_cleanroomsml.types.collaboration_trained_model_inference_job_list.deserialize_json(
                data["collaborationTrainedModelInferenceJobs"]
            )
        )
    else:
        raise DeserializationError(
            "ListCollaborationTrainedModelInferenceJobsResponse.collaboration_trained_model_inference_jobs required"
        )
    return out
