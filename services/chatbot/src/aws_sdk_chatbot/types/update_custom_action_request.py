"""Generated from Smithy shape ``com.amazonaws.chatbot#UpdateCustomActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chatbot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.custom_action_alias_name
    import aws_sdk_chatbot.types.custom_action_arn
    import aws_sdk_chatbot.types.custom_action_attachment_list
    import aws_sdk_chatbot.types.custom_action_definition


class UpdateCustomActionRequest(TypedDict, closed=True):
    custom_action_arn: "aws_sdk_chatbot.types.custom_action_arn.CustomActionArn"
    """<p>The fully defined Amazon Resource Name (ARN) of the custom action.</p>"""
    definition: "aws_sdk_chatbot.types.custom_action_definition.CustomActionDefinition"
    """<p>The definition of the command to run when invoked as an alias or as an action button.</p>"""
    alias_name: NotRequired[
        "aws_sdk_chatbot.types.custom_action_alias_name.CustomActionAliasName"
    ]
    """<p>The name used to invoke this action in the chat channel. For example, <code>@aws run my-alias</code>.</p>"""
    attachments: NotRequired[
        "aws_sdk_chatbot.types.custom_action_attachment_list.CustomActionAttachmentList"
    ]
    """<p>Defines when this custom action button should be attached to a notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCustomActionRequest) -> dict:
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
    return out


def deserialize_json(data: dict) -> UpdateCustomActionRequest:
    out: UpdateCustomActionRequest = {}  # type: ignore[typeddict-item]
    if "CustomActionArn" in data:
        out["custom_action_arn"] = data["CustomActionArn"]
    else:
        raise DeserializationError(
            "UpdateCustomActionRequest.custom_action_arn required"
        )
    if "Definition" in data:
        import aws_sdk_chatbot.types.custom_action_definition

        out["definition"] = (
            aws_sdk_chatbot.types.custom_action_definition.deserialize_json(
                data["Definition"]
            )
        )
    else:
        raise DeserializationError("UpdateCustomActionRequest.definition required")
    if "AliasName" in data:
        out["alias_name"] = data["AliasName"]
    if "Attachments" in data:
        import aws_sdk_chatbot.types.custom_action_attachment_list

        out["attachments"] = (
            aws_sdk_chatbot.types.custom_action_attachment_list.deserialize_json(
                data["Attachments"]
            )
        )
    return out
