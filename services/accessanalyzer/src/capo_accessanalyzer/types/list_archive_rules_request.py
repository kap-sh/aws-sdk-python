"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ListArchiveRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.analyzer_name
    import capo_accessanalyzer.types.token


class ListArchiveRulesRequest(TypedDict, closed=True):
    analyzer_name: "capo_accessanalyzer.types.analyzer_name.AnalyzerName"
    """<p>The name of the analyzer to retrieve rules from.</p>"""
    next_token: NotRequired["capo_accessanalyzer.types.token.Token"]
    """<p>A token used for pagination of results returned.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListArchiveRulesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListArchiveRulesRequest:
    out: ListArchiveRulesRequest = {}  # type: ignore[typeddict-item]
    return out
