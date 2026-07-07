"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CreatePrivacyBudgetTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.privacy_budget_template_auto_refresh
    import aws_sdk_cleanrooms.types.privacy_budget_template_parameters_input
    import aws_sdk_cleanrooms.types.privacy_budget_type
    import aws_sdk_cleanrooms.types.tag_map


class CreatePrivacyBudgetTemplateInput(TypedDict, closed=True):
    membership_identifier: (
        "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>A unique identifier for one of your memberships for a collaboration. The privacy budget template is created in the collaboration that this membership belongs to. Accepts a membership ID.</p>"""
    auto_refresh: NotRequired[
        "aws_sdk_cleanrooms.types.privacy_budget_template_auto_refresh.PrivacyBudgetTemplateAutoRefresh"
    ]
    """<p>How often the privacy budget refreshes.</p> <important> <p>If you plan to regularly bring new data into the collaboration, you can use <code>CALENDAR_MONTH</code> to automatically get a new privacy budget for the collaboration every calendar month. Choosing this option allows arbitrary amounts of information to be revealed about rows of the data when repeatedly queries across refreshes. Avoid choosing this if the same rows will be repeatedly queried between privacy budget refreshes.</p> </important>"""
    privacy_budget_type: (
        "aws_sdk_cleanrooms.types.privacy_budget_type.PrivacyBudgetType"
    )
    """<p>Specifies the type of the privacy budget template.</p>"""
    parameters: "aws_sdk_cleanrooms.types.privacy_budget_template_parameters_input.PrivacyBudgetTemplateParametersInput"
    """<p>Specifies your parameters for the privacy budget template.</p>"""
    tags: NotRequired["aws_sdk_cleanrooms.types.tag_map.TagMap"]
    """<p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePrivacyBudgetTemplateInput) -> dict:
    out: dict = {}
    if "auto_refresh" in value:
        import aws_sdk_cleanrooms.types.privacy_budget_template_auto_refresh

        out["autoRefresh"] = (
            aws_sdk_cleanrooms.types.privacy_budget_template_auto_refresh.serialize_json(
                value["auto_refresh"]
            )
        )
    import aws_sdk_cleanrooms.types.privacy_budget_type

    out["privacyBudgetType"] = (
        aws_sdk_cleanrooms.types.privacy_budget_type.serialize_json(
            value["privacy_budget_type"]
        )
    )
    import aws_sdk_cleanrooms.types.privacy_budget_template_parameters_input

    out["parameters"] = (
        aws_sdk_cleanrooms.types.privacy_budget_template_parameters_input.serialize_json(
            value["parameters"]
        )
    )
    if "tags" in value:
        import aws_sdk_cleanrooms.types.tag_map

        out["tags"] = aws_sdk_cleanrooms.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreatePrivacyBudgetTemplateInput:
    out: CreatePrivacyBudgetTemplateInput = {}  # type: ignore[typeddict-item]
    if "autoRefresh" in data:
        import aws_sdk_cleanrooms.types.privacy_budget_template_auto_refresh

        out["auto_refresh"] = (
            aws_sdk_cleanrooms.types.privacy_budget_template_auto_refresh.deserialize_json(
                data["autoRefresh"]
            )
        )
    if "privacyBudgetType" in data:
        import aws_sdk_cleanrooms.types.privacy_budget_type

        out["privacy_budget_type"] = (
            aws_sdk_cleanrooms.types.privacy_budget_type.deserialize_json(
                data["privacyBudgetType"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePrivacyBudgetTemplateInput.privacy_budget_type required"
        )
    if "parameters" in data:
        import aws_sdk_cleanrooms.types.privacy_budget_template_parameters_input

        out["parameters"] = (
            aws_sdk_cleanrooms.types.privacy_budget_template_parameters_input.deserialize_json(
                data["parameters"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePrivacyBudgetTemplateInput.parameters required"
        )
    if "tags" in data:
        import aws_sdk_cleanrooms.types.tag_map

        out["tags"] = aws_sdk_cleanrooms.types.tag_map.deserialize_json(data["tags"])
    return out
