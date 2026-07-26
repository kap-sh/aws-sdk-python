"""Generated from Smithy shape ``com.amazonaws.rum#ListAppMonitorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rum.types.max_results_integer


class ListAppMonitorsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_rum.types.max_results_integer.MaxResultsInteger"]
    """<p>The maximum number of results to return in one operation. The default is 50. The maximum that you can specify is 100.</p>"""
    next_token: NotRequired["str"]
    """<p>Use the token returned by the previous operation to request the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppMonitorsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAppMonitorsRequest:
    out: ListAppMonitorsRequest = {}  # type: ignore[typeddict-item]
    return out
