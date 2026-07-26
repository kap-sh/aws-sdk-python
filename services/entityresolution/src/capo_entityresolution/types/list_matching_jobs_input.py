"""Generated from Smithy shape ``com.amazonaws.entityresolution#ListMatchingJobsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.entity_name
    import capo_entityresolution.types.next_token


class ListMatchingJobsInput(TypedDict, closed=True):
    workflow_name: "capo_entityresolution.types.entity_name.EntityName"
    """<p>The name of the workflow to be retrieved.</p>"""
    next_token: NotRequired["capo_entityresolution.types.next_token.NextToken"]
    """<p>The pagination token from the previous API call.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of objects returned per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMatchingJobsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMatchingJobsInput:
    out: ListMatchingJobsInput = {}  # type: ignore[typeddict-item]
    return out
