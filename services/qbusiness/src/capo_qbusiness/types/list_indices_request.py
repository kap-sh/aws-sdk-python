"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListIndicesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.max_results_integer_for_list_indices
    import capo_qbusiness.types.next_token


class ListIndicesRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application connected to the index.</p>"""
    next_token: NotRequired["capo_qbusiness.types.next_token.NextToken"]
    """<p>If the maxResults response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of Amazon Q Business indices.</p>"""
    max_results: NotRequired[
        "capo_qbusiness.types.max_results_integer_for_list_indices.MaxResultsIntegerForListIndices"
    ]
    """<p>The maximum number of indices to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIndicesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListIndicesRequest:
    out: ListIndicesRequest = {}  # type: ignore[typeddict-item]
    return out
