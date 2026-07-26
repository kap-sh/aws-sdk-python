"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#GetAnalyzerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.analyzer_name


class GetAnalyzerRequest(TypedDict, closed=True):
    analyzer_name: "capo_accessanalyzer.types.analyzer_name.AnalyzerName"
    """<p>The name of the analyzer retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAnalyzerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAnalyzerRequest:
    out: GetAnalyzerRequest = {}  # type: ignore[typeddict-item]
    return out
