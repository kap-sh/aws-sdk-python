"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateConfiguredTableAnalysisRuleOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.configured_table_analysis_rule


class UpdateConfiguredTableAnalysisRuleOutput(TypedDict):
    analysis_rule: "aws_sdk_cleanrooms.types.configured_table_analysis_rule.ConfiguredTableAnalysisRule"
    """<p>The entire updated analysis rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfiguredTableAnalysisRuleOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.configured_table_analysis_rule

    out["analysisRule"] = (
        aws_sdk_cleanrooms.types.configured_table_analysis_rule.serialize_json(
            value["analysis_rule"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateConfiguredTableAnalysisRuleOutput:
    out: UpdateConfiguredTableAnalysisRuleOutput = {}  # type: ignore[typeddict-item]
    if "analysisRule" in data:
        import aws_sdk_cleanrooms.types.configured_table_analysis_rule

        out["analysis_rule"] = (
            aws_sdk_cleanrooms.types.configured_table_analysis_rule.deserialize_json(
                data["analysisRule"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateConfiguredTableAnalysisRuleOutput.analysis_rule required"
        )
    return out
