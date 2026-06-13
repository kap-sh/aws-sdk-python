"""Generated from Smithy shape ``com.amazonaws.backupsearch#ListSearchJobResultsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backupsearch.types.generic_id


class ListSearchJobResultsInput(TypedDict):
    search_job_identifier: "aws_sdk_backupsearch.types.generic_id.GenericId"
    """<p>The unique string that specifies the search job.</p>"""
    next_token: NotRequired["str"]
    """<p>The next item following a partial list of returned search job results.</p> <p>For example, if a request is made to return <code>MaxResults</code> number of search job results, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""
    max_results: "int"
    """<p>The maximum number of resource list items to be returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSearchJobResultsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSearchJobResultsInput:
    out: ListSearchJobResultsInput = {}  # type: ignore[typeddict-item]
    return out
