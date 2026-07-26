"""Generated from Smithy shape ``com.amazonaws.chatbot#CustomActionAttachment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chatbot.types.custom_action_attachment_criteria_list
    import capo_chatbot.types.custom_action_attachment_notification_type
    import capo_chatbot.types.custom_action_attachment_variables
    import capo_chatbot.types.custom_action_button_text


class CustomActionAttachment(TypedDict, closed=True):
    notification_type: NotRequired[
        "capo_chatbot.types.custom_action_attachment_notification_type.CustomActionAttachmentNotificationType"
    ]
    """<p>The type of notification that the custom action should be attached to.</p>"""
    button_text: NotRequired[
        "capo_chatbot.types.custom_action_button_text.CustomActionButtonText"
    ]
    """<p>The text of the button that appears on the notification.</p>"""
    criteria: NotRequired[
        "capo_chatbot.types.custom_action_attachment_criteria_list.CustomActionAttachmentCriteriaList"
    ]
    """<p>The criteria for when a button should be shown based on values in the notification.</p>"""
    variables: NotRequired[
        "capo_chatbot.types.custom_action_attachment_variables.CustomActionAttachmentVariables"
    ]
    """<p>The variables to extract from the notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomActionAttachment) -> dict:
    out: dict = {}
    if "notification_type" in value:
        out["NotificationType"] = value["notification_type"]
    if "button_text" in value:
        out["ButtonText"] = value["button_text"]
    if "criteria" in value:
        import capo_chatbot.types.custom_action_attachment_criteria_list

        out["Criteria"] = (
            capo_chatbot.types.custom_action_attachment_criteria_list.serialize_json(
                value["criteria"]
            )
        )
    if "variables" in value:
        import capo_chatbot.types.custom_action_attachment_variables

        out["Variables"] = (
            capo_chatbot.types.custom_action_attachment_variables.serialize_json(
                value["variables"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomActionAttachment:
    out: CustomActionAttachment = {}  # type: ignore[typeddict-item]
    if "NotificationType" in data:
        out["notification_type"] = data["NotificationType"]
    if "ButtonText" in data:
        out["button_text"] = data["ButtonText"]
    if "Criteria" in data:
        import capo_chatbot.types.custom_action_attachment_criteria_list

        out["criteria"] = (
            capo_chatbot.types.custom_action_attachment_criteria_list.deserialize_json(
                data["Criteria"]
            )
        )
    if "Variables" in data:
        import capo_chatbot.types.custom_action_attachment_variables

        out["variables"] = (
            capo_chatbot.types.custom_action_attachment_variables.deserialize_json(
                data["Variables"]
            )
        )
    return out
