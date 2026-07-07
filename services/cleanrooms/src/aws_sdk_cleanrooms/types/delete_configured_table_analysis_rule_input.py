"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DeleteConfiguredTableAnalysisRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.configured_table_analysis_rule_type
    import aws_sdk_cleanrooms.types.configured_table_identifier


class DeleteConfiguredTableAnalysisRuleInput(TypedDict, closed=True):
    configured_table_identifier: (
        "aws_sdk_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier"
    )
    """<p>The unique identifier for the configured table that the analysis rule applies to. Currently accepts the configured table ID.</p>"""
    analysis_rule_type: "aws_sdk_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType"
    """<p>The analysis rule type to be deleted. Configured table analysis rules are uniquely identified by their configured table identifier and analysis rule type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConfiguredTableAnalysisRuleInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConfiguredTableAnalysisRuleInput:
    out: DeleteConfiguredTableAnalysisRuleInput = {}  # type: ignore[typeddict-item]
    return out
