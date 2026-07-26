"""Generated from Smithy shape ``com.amazonaws.wisdom#ListImportJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wisdom.types.max_results
    import capo_wisdom.types.non_empty_string
    import capo_wisdom.types.uuid_or_arn


class ListImportJobsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_wisdom.types.non_empty_string.NonEmptyString"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_wisdom.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""
    knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImportJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListImportJobsRequest:
    out: ListImportJobsRequest = {}  # type: ignore[typeddict-item]
    return out
