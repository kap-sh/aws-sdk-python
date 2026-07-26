"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetAnalysisTemplateOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_template


class GetAnalysisTemplateOutput(TypedDict, closed=True):
    analysis_template: "capo_cleanrooms.types.analysis_template.AnalysisTemplate"
    """<p>The analysis template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAnalysisTemplateOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.analysis_template

    out["analysisTemplate"] = capo_cleanrooms.types.analysis_template.serialize_json(
        value["analysis_template"]
    )
    return out


def deserialize_json(data: dict) -> GetAnalysisTemplateOutput:
    out: GetAnalysisTemplateOutput = {}  # type: ignore[typeddict-item]
    if "analysisTemplate" in data:
        import capo_cleanrooms.types.analysis_template

        out["analysis_template"] = (
            capo_cleanrooms.types.analysis_template.deserialize_json(
                data["analysisTemplate"]
            )
        )
    else:
        raise DeserializationError(
            "GetAnalysisTemplateOutput.analysis_template required"
        )
    return out
