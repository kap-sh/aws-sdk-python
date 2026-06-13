"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateConfiguredTableAssociationAnalysisRuleInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_policy
    import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type
    import aws_sdk_cleanrooms.types.configured_table_association_identifier
    import aws_sdk_cleanrooms.types.membership_identifier


class UpdateConfiguredTableAssociationAnalysisRuleInput(TypedDict):
    membership_identifier: (
        "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p> A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>"""
    configured_table_association_identifier: "aws_sdk_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier"
    """<p> The identifier for the configured table association to update.</p>"""
    analysis_rule_type: "aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type.ConfiguredTableAssociationAnalysisRuleType"
    """<p> The analysis rule type that you want to update.</p>"""
    analysis_rule_policy: "aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_policy.ConfiguredTableAssociationAnalysisRulePolicy"
    """<p> The updated analysis rule policy for the conﬁgured table association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfiguredTableAssociationAnalysisRuleInput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_policy

    out["analysisRulePolicy"] = (
        aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_policy.serialize_json(
            value["analysis_rule_policy"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateConfiguredTableAssociationAnalysisRuleInput:
    out: UpdateConfiguredTableAssociationAnalysisRuleInput = {}  # type: ignore[typeddict-item]
    if "analysisRulePolicy" in data:
        import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_policy

        out["analysis_rule_policy"] = (
            aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_policy.deserialize_json(
                data["analysisRulePolicy"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateConfiguredTableAssociationAnalysisRuleInput.analysis_rule_policy required"
        )
    return out
