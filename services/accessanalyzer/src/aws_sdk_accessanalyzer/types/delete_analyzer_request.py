"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#DeleteAnalyzerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.analyzer_name


class DeleteAnalyzerRequest(TypedDict, closed=True):
    analyzer_name: "aws_sdk_accessanalyzer.types.analyzer_name.AnalyzerName"
    """<p>The name of the analyzer to delete.</p>"""
    client_token: NotRequired["str"]
    """<p>A client token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAnalyzerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAnalyzerRequest:
    out: DeleteAnalyzerRequest = {}  # type: ignore[typeddict-item]
    return out
