"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdatePrivacyBudgetTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.privacy_budget_template_identifier
    import aws_sdk_cleanrooms.types.privacy_budget_template_update_parameters
    import aws_sdk_cleanrooms.types.privacy_budget_type


class UpdatePrivacyBudgetTemplateInput(TypedDict, closed=True):
    membership_identifier: (
        "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>A unique identifier for one of your memberships for a collaboration. The privacy budget template is updated in the collaboration that this membership belongs to. Accepts a membership ID.</p>"""
    privacy_budget_template_identifier: "aws_sdk_cleanrooms.types.privacy_budget_template_identifier.PrivacyBudgetTemplateIdentifier"
    """<p>A unique identifier for your privacy budget template that you want to update.</p>"""
    privacy_budget_type: (
        "aws_sdk_cleanrooms.types.privacy_budget_type.PrivacyBudgetType"
    )
    """<p>Specifies the type of the privacy budget template.</p>"""
    parameters: NotRequired[
        "aws_sdk_cleanrooms.types.privacy_budget_template_update_parameters.PrivacyBudgetTemplateUpdateParameters"
    ]
    """<p>Specifies the epsilon and noise parameters for the privacy budget template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePrivacyBudgetTemplateInput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.privacy_budget_type

    out["privacyBudgetType"] = (
        aws_sdk_cleanrooms.types.privacy_budget_type.serialize_json(
            value["privacy_budget_type"]
        )
    )
    if "parameters" in value:
        import aws_sdk_cleanrooms.types.privacy_budget_template_update_parameters

        out["parameters"] = (
            aws_sdk_cleanrooms.types.privacy_budget_template_update_parameters.serialize_json(
                value["parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatePrivacyBudgetTemplateInput:
    out: UpdatePrivacyBudgetTemplateInput = {}  # type: ignore[typeddict-item]
    if "privacyBudgetType" in data:
        import aws_sdk_cleanrooms.types.privacy_budget_type

        out["privacy_budget_type"] = (
            aws_sdk_cleanrooms.types.privacy_budget_type.deserialize_json(
                data["privacyBudgetType"]
            )
        )
    else:
        raise DeserializationError(
            "UpdatePrivacyBudgetTemplateInput.privacy_budget_type required"
        )
    if "parameters" in data:
        import aws_sdk_cleanrooms.types.privacy_budget_template_update_parameters

        out["parameters"] = (
            aws_sdk_cleanrooms.types.privacy_budget_template_update_parameters.deserialize_json(
                data["parameters"]
            )
        )
    return out
