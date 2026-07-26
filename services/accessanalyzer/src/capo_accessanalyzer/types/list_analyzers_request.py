"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ListAnalyzersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.token
    import capo_accessanalyzer.types.type


class ListAnalyzersRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_accessanalyzer.types.token.Token"]
    """<p>A token used for pagination of results returned.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in the response.</p>"""
    type: NotRequired["capo_accessanalyzer.types.type.Type"]
    """<p>The type of analyzer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnalyzersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAnalyzersRequest:
    out: ListAnalyzersRequest = {}  # type: ignore[typeddict-item]
    return out
