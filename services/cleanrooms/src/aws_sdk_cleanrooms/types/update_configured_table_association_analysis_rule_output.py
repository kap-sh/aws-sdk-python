"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateConfiguredTableAssociationAnalysisRuleOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule


class UpdateConfiguredTableAssociationAnalysisRuleOutput(TypedDict):
    analysis_rule: "aws_sdk_cleanrooms.types.configured_table_association_analysis_rule.ConfiguredTableAssociationAnalysisRule"
    """<p> The updated analysis rule for the conﬁgured table association. In the console, the <code>ConfiguredTableAssociationAnalysisRule</code> is referred to as the <i>collaboration analysis rule</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfiguredTableAssociationAnalysisRuleOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule

    out["analysisRule"] = (
        aws_sdk_cleanrooms.types.configured_table_association_analysis_rule.serialize_json(
            value["analysis_rule"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateConfiguredTableAssociationAnalysisRuleOutput:
    out: UpdateConfiguredTableAssociationAnalysisRuleOutput = {}  # type: ignore[typeddict-item]
    if "analysisRule" in data:
        import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule

        out["analysis_rule"] = (
            aws_sdk_cleanrooms.types.configured_table_association_analysis_rule.deserialize_json(
                data["analysisRule"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateConfiguredTableAssociationAnalysisRuleOutput.analysis_rule required"
        )
    return out
