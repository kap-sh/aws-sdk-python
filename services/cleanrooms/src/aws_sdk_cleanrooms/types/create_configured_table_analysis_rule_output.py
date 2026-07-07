"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CreateConfiguredTableAnalysisRuleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.configured_table_analysis_rule


class CreateConfiguredTableAnalysisRuleOutput(TypedDict, closed=True):
    analysis_rule: "aws_sdk_cleanrooms.types.configured_table_analysis_rule.ConfiguredTableAnalysisRule"
    """<p>The analysis rule that was created for the configured table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfiguredTableAnalysisRuleOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.configured_table_analysis_rule

    out["analysisRule"] = (
        aws_sdk_cleanrooms.types.configured_table_analysis_rule.serialize_json(
            value["analysis_rule"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateConfiguredTableAnalysisRuleOutput:
    out: CreateConfiguredTableAnalysisRuleOutput = {}  # type: ignore[typeddict-item]
    if "analysisRule" in data:
        import aws_sdk_cleanrooms.types.configured_table_analysis_rule

        out["analysis_rule"] = (
            aws_sdk_cleanrooms.types.configured_table_analysis_rule.deserialize_json(
                data["analysisRule"]
            )
        )
    else:
        raise DeserializationError(
            "CreateConfiguredTableAnalysisRuleOutput.analysis_rule required"
        )
    return out
