"""Generated from Smithy shape ``com.amazonaws.chatbot#CustomAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chatbot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.custom_action_alias_name
    import aws_sdk_chatbot.types.custom_action_arn
    import aws_sdk_chatbot.types.custom_action_attachment_list
    import aws_sdk_chatbot.types.custom_action_definition
    import aws_sdk_chatbot.types.custom_action_name


class CustomAction(TypedDict):
    custom_action_arn: "aws_sdk_chatbot.types.custom_action_arn.CustomActionArn"
    """<p>The fully defined Amazon Resource Name (ARN) of the custom action.</p>"""
    definition: "aws_sdk_chatbot.types.custom_action_definition.CustomActionDefinition"
    """<p>The definition of the command to run when invoked an alias or as an action button.</p>"""
    alias_name: NotRequired[
        "aws_sdk_chatbot.types.custom_action_alias_name.CustomActionAliasName"
    ]
    """<p>The name used to invoke this action in the chat channel. For example, <code>@aws run my-alias</code>.</p>"""
    attachments: NotRequired[
        "aws_sdk_chatbot.types.custom_action_attachment_list.CustomActionAttachmentList"
    ]
    """<p>Defines when this custom action button should be attached to a notification.</p>"""
    action_name: NotRequired[
        "aws_sdk_chatbot.types.custom_action_name.CustomActionName"
    ]
    """<p>The name of the custom action that is included in the ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomAction) -> dict:
    out: dict = {}
    out["CustomActionArn"] = value["custom_action_arn"]
    import aws_sdk_chatbot.types.custom_action_definition

    out["Definition"] = aws_sdk_chatbot.types.custom_action_definition.serialize_json(
        value["definition"]
    )
    if "alias_name" in value:
        out["AliasName"] = value["alias_name"]
    if "attachments" in value:
        import aws_sdk_chatbot.types.custom_action_attachment_list

        out["Attachments"] = (
            aws_sdk_chatbot.types.custom_action_attachment_list.serialize_json(
                value["attachments"]
            )
        )
    if "action_name" in value:
        out["ActionName"] = value["action_name"]
    return out


def deserialize_json(data: dict) -> CustomAction:
    out: CustomAction = {}  # type: ignore[typeddict-item]
    if "CustomActionArn" in data:
        out["custom_action_arn"] = data["CustomActionArn"]
    else:
        raise DeserializationError("CustomAction.custom_action_arn required")
    if "Definition" in data:
        import aws_sdk_chatbot.types.custom_action_definition

        out["definition"] = (
            aws_sdk_chatbot.types.custom_action_definition.deserialize_json(
                data["Definition"]
            )
        )
    else:
        raise DeserializationError("CustomAction.definition required")
    if "AliasName" in data:
        out["alias_name"] = data["AliasName"]
    if "Attachments" in data:
        import aws_sdk_chatbot.types.custom_action_attachment_list

        out["attachments"] = (
            aws_sdk_chatbot.types.custom_action_attachment_list.deserialize_json(
                data["Attachments"]
            )
        )
    if "ActionName" in data:
        out["action_name"] = data["ActionName"]
    return out
