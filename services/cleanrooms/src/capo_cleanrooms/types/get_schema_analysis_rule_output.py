"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetSchemaAnalysisRuleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_rule


class GetSchemaAnalysisRuleOutput(TypedDict, closed=True):
    analysis_rule: "capo_cleanrooms.types.analysis_rule.AnalysisRule"
    """<p>A specification about how data from the configured table can be used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSchemaAnalysisRuleOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.analysis_rule

    out["analysisRule"] = capo_cleanrooms.types.analysis_rule.serialize_json(
        value["analysis_rule"]
    )
    return out


def deserialize_json(data: dict) -> GetSchemaAnalysisRuleOutput:
    out: GetSchemaAnalysisRuleOutput = {}  # type: ignore[typeddict-item]
    if "analysisRule" in data:
        import capo_cleanrooms.types.analysis_rule

        out["analysis_rule"] = capo_cleanrooms.types.analysis_rule.deserialize_json(
            data["analysisRule"]
        )
    else:
        raise DeserializationError("GetSchemaAnalysisRuleOutput.analysis_rule required")
    return out
