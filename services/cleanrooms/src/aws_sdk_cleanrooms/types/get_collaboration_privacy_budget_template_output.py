"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetCollaborationPrivacyBudgetTemplateOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.collaboration_privacy_budget_template


class GetCollaborationPrivacyBudgetTemplateOutput(TypedDict):
    collaboration_privacy_budget_template: "aws_sdk_cleanrooms.types.collaboration_privacy_budget_template.CollaborationPrivacyBudgetTemplate"
    """<p>Returns the details of the privacy budget template that you requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCollaborationPrivacyBudgetTemplateOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.collaboration_privacy_budget_template

    out["collaborationPrivacyBudgetTemplate"] = (
        aws_sdk_cleanrooms.types.collaboration_privacy_budget_template.serialize_json(
            value["collaboration_privacy_budget_template"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetCollaborationPrivacyBudgetTemplateOutput:
    out: GetCollaborationPrivacyBudgetTemplateOutput = {}  # type: ignore[typeddict-item]
    if "collaborationPrivacyBudgetTemplate" in data:
        import aws_sdk_cleanrooms.types.collaboration_privacy_budget_template

        out["collaboration_privacy_budget_template"] = (
            aws_sdk_cleanrooms.types.collaboration_privacy_budget_template.deserialize_json(
                data["collaborationPrivacyBudgetTemplate"]
            )
        )
    else:
        raise DeserializationError(
            "GetCollaborationPrivacyBudgetTemplateOutput.collaboration_privacy_budget_template required"
        )
    return out
