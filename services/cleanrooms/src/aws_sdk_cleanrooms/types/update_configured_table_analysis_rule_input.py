"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateConfiguredTableAnalysisRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.configured_table_analysis_rule_policy
    import aws_sdk_cleanrooms.types.configured_table_analysis_rule_type
    import aws_sdk_cleanrooms.types.configured_table_identifier


class UpdateConfiguredTableAnalysisRuleInput(TypedDict, closed=True):
    configured_table_identifier: (
        "aws_sdk_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier"
    )
    """<p>The unique identifier for the configured table that the analysis rule applies to. Currently accepts the configured table ID.</p>"""
    analysis_rule_type: "aws_sdk_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType"
    """<p>The analysis rule type to be updated. Configured table analysis rules are uniquely identified by their configured table identifier and analysis rule type.</p>"""
    analysis_rule_policy: "aws_sdk_cleanrooms.types.configured_table_analysis_rule_policy.ConfiguredTableAnalysisRulePolicy"
    """<p>The new analysis rule policy for the configured table analysis rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfiguredTableAnalysisRuleInput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.configured_table_analysis_rule_policy

    out["analysisRulePolicy"] = (
        aws_sdk_cleanrooms.types.configured_table_analysis_rule_policy.serialize_json(
            value["analysis_rule_policy"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateConfiguredTableAnalysisRuleInput:
    out: UpdateConfiguredTableAnalysisRuleInput = {}  # type: ignore[typeddict-item]
    if "analysisRulePolicy" in data:
        import aws_sdk_cleanrooms.types.configured_table_analysis_rule_policy

        out["analysis_rule_policy"] = (
            aws_sdk_cleanrooms.types.configured_table_analysis_rule_policy.deserialize_json(
                data["analysisRulePolicy"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateConfiguredTableAnalysisRuleInput.analysis_rule_policy required"
        )
    return out
