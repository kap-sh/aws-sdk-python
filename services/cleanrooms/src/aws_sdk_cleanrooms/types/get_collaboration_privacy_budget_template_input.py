"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetCollaborationPrivacyBudgetTemplateInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.collaboration_identifier
    import aws_sdk_cleanrooms.types.privacy_budget_template_identifier


class GetCollaborationPrivacyBudgetTemplateInput(TypedDict):
    collaboration_identifier: (
        "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>A unique identifier for one of your collaborations.</p>"""
    privacy_budget_template_identifier: "aws_sdk_cleanrooms.types.privacy_budget_template_identifier.PrivacyBudgetTemplateIdentifier"
    """<p>A unique identifier for one of your privacy budget templates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCollaborationPrivacyBudgetTemplateInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCollaborationPrivacyBudgetTemplateInput:
    out: GetCollaborationPrivacyBudgetTemplateInput = {}  # type: ignore[typeddict-item]
    return out
