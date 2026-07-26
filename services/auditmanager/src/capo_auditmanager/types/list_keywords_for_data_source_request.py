"""Generated from Smithy shape ``com.amazonaws.auditmanager#ListKeywordsForDataSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.data_source_type
    import capo_auditmanager.types.max_results
    import capo_auditmanager.types.token


class ListKeywordsForDataSourceRequest(TypedDict, closed=True):
    source: "capo_auditmanager.types.data_source_type.DataSourceType"
    """<p>The control mapping data source that the keywords apply to. </p>"""
    next_token: NotRequired["capo_auditmanager.types.token.Token"]
    """<p> The pagination token that's used to fetch the next set of results. </p>"""
    max_results: NotRequired["capo_auditmanager.types.max_results.MaxResults"]
    """<p> Represents the maximum number of results on a page or for an API request call. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKeywordsForDataSourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListKeywordsForDataSourceRequest:
    out: ListKeywordsForDataSourceRequest = {}  # type: ignore[typeddict-item]
    return out
