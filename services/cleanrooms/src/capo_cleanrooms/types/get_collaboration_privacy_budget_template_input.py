"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetCollaborationPrivacyBudgetTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.collaboration_identifier
    import capo_cleanrooms.types.privacy_budget_template_identifier


class GetCollaborationPrivacyBudgetTemplateInput(TypedDict, closed=True):
    collaboration_identifier: (
        "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>A unique identifier for one of your collaborations.</p>"""
    privacy_budget_template_identifier: "capo_cleanrooms.types.privacy_budget_template_identifier.PrivacyBudgetTemplateIdentifier"
    """<p>A unique identifier for one of your privacy budget templates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCollaborationPrivacyBudgetTemplateInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCollaborationPrivacyBudgetTemplateInput:
    out: GetCollaborationPrivacyBudgetTemplateInput = {}  # type: ignore[typeddict-item]
    return out
