"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateConfiguredTableAnalysisRuleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.configured_table_analysis_rule


class UpdateConfiguredTableAnalysisRuleOutput(TypedDict, closed=True):
    analysis_rule: "capo_cleanrooms.types.configured_table_analysis_rule.ConfiguredTableAnalysisRule"
    """<p>The entire updated analysis rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfiguredTableAnalysisRuleOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.configured_table_analysis_rule

    out["analysisRule"] = (
        capo_cleanrooms.types.configured_table_analysis_rule.serialize_json(
            value["analysis_rule"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateConfiguredTableAnalysisRuleOutput:
    out: UpdateConfiguredTableAnalysisRuleOutput = {}  # type: ignore[typeddict-item]
    if "analysisRule" in data:
        import capo_cleanrooms.types.configured_table_analysis_rule

        out["analysis_rule"] = (
            capo_cleanrooms.types.configured_table_analysis_rule.deserialize_json(
                data["analysisRule"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateConfiguredTableAnalysisRuleOutput.analysis_rule required"
        )
    return out
