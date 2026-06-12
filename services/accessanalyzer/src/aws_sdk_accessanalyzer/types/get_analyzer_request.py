"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#GetAnalyzerRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.analyzer_name


class GetAnalyzerRequest(TypedDict):
    analyzer_name: "aws_sdk_accessanalyzer.types.analyzer_name.AnalyzerName"
    """<p>The name of the analyzer retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAnalyzerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAnalyzerRequest:
    out: GetAnalyzerRequest = {}  # type: ignore[typeddict-item]
    return out
