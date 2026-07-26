"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListAudienceGenerationJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.configured_audience_model_arn
    import capo_cleanroomsml.types.max_results
    import capo_cleanroomsml.types.next_token
    import capo_cleanroomsml.types.uuid


class ListAudienceGenerationJobsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value retrieved from a previous call to access the next page of results.</p>"""
    max_results: NotRequired["capo_cleanroomsml.types.max_results.MaxResults"]
    """<p>The maximum size of the results that is returned per call.</p>"""
    configured_audience_model_arn: NotRequired[
        "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the configured audience model that was used for the audience generation jobs that you are interested in.</p>"""
    collaboration_id: NotRequired["capo_cleanroomsml.types.uuid.UUID"]
    """<p>The identifier of the collaboration that contains the audience generation jobs that you are interested in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAudienceGenerationJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAudienceGenerationJobsRequest:
    out: ListAudienceGenerationJobsRequest = {}  # type: ignore[typeddict-item]
    return out
