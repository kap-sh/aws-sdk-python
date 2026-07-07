"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DeletePrivacyBudgetTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.privacy_budget_template_identifier


class DeletePrivacyBudgetTemplateInput(TypedDict, closed=True):
    membership_identifier: (
        "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>A unique identifier for one of your memberships for a collaboration. The privacy budget template is deleted from the collaboration that this membership belongs to. Accepts a membership ID.</p>"""
    privacy_budget_template_identifier: "aws_sdk_cleanrooms.types.privacy_budget_template_identifier.PrivacyBudgetTemplateIdentifier"
    """<p>A unique identifier for your privacy budget template. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePrivacyBudgetTemplateInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePrivacyBudgetTemplateInput:
    out: DeletePrivacyBudgetTemplateInput = {}  # type: ignore[typeddict-item]
    return out
