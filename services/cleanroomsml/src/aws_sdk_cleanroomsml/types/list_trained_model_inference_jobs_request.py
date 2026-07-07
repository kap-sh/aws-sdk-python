"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListTrainedModelInferenceJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.max_results
    import aws_sdk_cleanroomsml.types.next_token
    import aws_sdk_cleanroomsml.types.trained_model_arn
    import aws_sdk_cleanroomsml.types.uuid


class ListTrainedModelInferenceJobsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value retrieved from a previous call to access the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_cleanroomsml.types.max_results.MaxResults"]
    """<p>The maximum size of the results that is returned per call.</p>"""
    membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID"
    """<p>The membership </p>"""
    trained_model_arn: NotRequired[
        "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a trained model that was used to create the trained model inference jobs that you are interested in.</p>"""
    trained_model_version_identifier: NotRequired[
        "aws_sdk_cleanroomsml.types.uuid.UUID"
    ]
    """<p>The version identifier of the trained model to filter inference jobs by. When specified, only inference jobs that used this specific version of the trained model are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTrainedModelInferenceJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTrainedModelInferenceJobsRequest:
    out: ListTrainedModelInferenceJobsRequest = {}  # type: ignore[typeddict-item]
    return out
