"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#GetAnalyzerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_accessanalyzer.types.analyzer_summary


class GetAnalyzerResponse(TypedDict, closed=True):
    analyzer: "capo_accessanalyzer.types.analyzer_summary.AnalyzerSummary"
    """<p>An <code>AnalyzerSummary</code> object that contains information about the analyzer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAnalyzerResponse) -> dict:
    out: dict = {}
    import capo_accessanalyzer.types.analyzer_summary

    out["analyzer"] = capo_accessanalyzer.types.analyzer_summary.serialize_json(
        value["analyzer"]
    )
    return out


def deserialize_json(data: dict) -> GetAnalyzerResponse:
    out: GetAnalyzerResponse = {}  # type: ignore[typeddict-item]
    if "analyzer" in data:
        import capo_accessanalyzer.types.analyzer_summary

        out["analyzer"] = capo_accessanalyzer.types.analyzer_summary.deserialize_json(
            data["analyzer"]
        )
    else:
        raise DeserializationError("GetAnalyzerResponse.analyzer required")
    return out
