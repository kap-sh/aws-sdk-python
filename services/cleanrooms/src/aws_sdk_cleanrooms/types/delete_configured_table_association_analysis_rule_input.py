"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DeleteConfiguredTableAssociationAnalysisRuleInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type
    import aws_sdk_cleanrooms.types.configured_table_association_identifier
    import aws_sdk_cleanrooms.types.membership_identifier


class DeleteConfiguredTableAssociationAnalysisRuleInput(TypedDict):
    membership_identifier: (
        "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p> A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>"""
    configured_table_association_identifier: "aws_sdk_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier"
    """<p>The identiﬁer for the conﬁgured table association that's related to the analysis rule that you want to delete.</p>"""
    analysis_rule_type: "aws_sdk_cleanrooms.types.configured_table_association_analysis_rule_type.ConfiguredTableAssociationAnalysisRuleType"
    """<p>The type of the analysis rule that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConfiguredTableAssociationAnalysisRuleInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConfiguredTableAssociationAnalysisRuleInput:
    out: DeleteConfiguredTableAssociationAnalysisRuleInput = {}  # type: ignore[typeddict-item]
    return out
