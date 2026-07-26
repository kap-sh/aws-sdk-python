"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListAudienceExportJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.audience_generation_job_arn
    import capo_cleanroomsml.types.max_results
    import capo_cleanroomsml.types.next_token


class ListAudienceExportJobsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value retrieved from a previous call to access the next page of results.</p>"""
    max_results: NotRequired["capo_cleanroomsml.types.max_results.MaxResults"]
    """<p>The maximum size of the results that is returned per call.</p>"""
    audience_generation_job_arn: NotRequired[
        "capo_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the audience generation job that you are interested in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAudienceExportJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAudienceExportJobsRequest:
    out: ListAudienceExportJobsRequest = {}  # type: ignore[typeddict-item]
    return out
