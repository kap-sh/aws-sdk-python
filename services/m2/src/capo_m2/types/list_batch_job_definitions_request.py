"""Generated from Smithy shape ``com.amazonaws.m2#ListBatchJobDefinitionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_m2.types.identifier
    import capo_m2.types.max_results
    import capo_m2.types.next_token


class ListBatchJobDefinitionsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_m2.types.next_token.NextToken"]
    """<p>A pagination token returned from a previous call to this operation. This specifies the next item to return. To return to the beginning of the list, exclude this parameter.</p>"""
    max_results: NotRequired["capo_m2.types.max_results.MaxResults"]
    """<p>The maximum number of batch job definitions to return.</p>"""
    application_id: "capo_m2.types.identifier.Identifier"
    """<p>The identifier of the application.</p>"""
    prefix: NotRequired["str"]
    """<p>If the batch job definition is a FileBatchJobDefinition, the prefix allows you to search on the file names of FileBatchJobDefinitions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBatchJobDefinitionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListBatchJobDefinitionsRequest:
    out: ListBatchJobDefinitionsRequest = {}  # type: ignore[typeddict-item]
    return out
