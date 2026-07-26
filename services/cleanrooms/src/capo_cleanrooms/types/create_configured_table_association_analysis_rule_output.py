"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CreateConfiguredTableAssociationAnalysisRuleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.configured_table_association_analysis_rule


class CreateConfiguredTableAssociationAnalysisRuleOutput(TypedDict, closed=True):
    analysis_rule: "capo_cleanrooms.types.configured_table_association_analysis_rule.ConfiguredTableAssociationAnalysisRule"
    """<p>The analysis rule for the conﬁgured table association. In the console, the <code>ConfiguredTableAssociationAnalysisRule</code> is referred to as the <i>collaboration analysis rule</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfiguredTableAssociationAnalysisRuleOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.configured_table_association_analysis_rule

    out["analysisRule"] = (
        capo_cleanrooms.types.configured_table_association_analysis_rule.serialize_json(
            value["analysis_rule"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateConfiguredTableAssociationAnalysisRuleOutput:
    out: CreateConfiguredTableAssociationAnalysisRuleOutput = {}  # type: ignore[typeddict-item]
    if "analysisRule" in data:
        import capo_cleanrooms.types.configured_table_association_analysis_rule

        out["analysis_rule"] = (
            capo_cleanrooms.types.configured_table_association_analysis_rule.deserialize_json(
                data["analysisRule"]
            )
        )
    else:
        raise DeserializationError(
            "CreateConfiguredTableAssociationAnalysisRuleOutput.analysis_rule required"
        )
    return out
