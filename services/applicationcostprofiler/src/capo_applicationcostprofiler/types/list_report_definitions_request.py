"""Generated from Smithy shape ``com.amazonaws.applicationcostprofiler#ListReportDefinitionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_applicationcostprofiler.types.integer
    import capo_applicationcostprofiler.types.token


class ListReportDefinitionsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_applicationcostprofiler.types.token.Token"]
    """<p>The token value from a previous call to access the next page of results.</p>"""
    max_results: NotRequired["capo_applicationcostprofiler.types.integer.Integer"]
    """<p>The maximum number of results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReportDefinitionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListReportDefinitionsRequest:
    out: ListReportDefinitionsRequest = {}  # type: ignore[typeddict-item]
    return out
