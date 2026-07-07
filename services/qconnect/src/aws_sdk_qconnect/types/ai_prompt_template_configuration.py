"""Generated from Smithy shape ``com.amazonaws.qconnect#AIPromptTemplateConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.text_full_ai_prompt_edit_template_configuration


class _AIPromptTemplateConfiguration_textFullAIPromptEditTemplateConfiguration(
    TypedDict, closed=True
):
    textFullAIPromptEditTemplateConfiguration: "aws_sdk_qconnect.types.text_full_ai_prompt_edit_template_configuration.TextFullAIPromptEditTemplateConfiguration"


AIPromptTemplateConfiguration: TypeAlias = (
    _AIPromptTemplateConfiguration_textFullAIPromptEditTemplateConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: AIPromptTemplateConfiguration) -> dict:
    if "textFullAIPromptEditTemplateConfiguration" in value:
        import aws_sdk_qconnect.types.text_full_ai_prompt_edit_template_configuration

        return {
            "textFullAIPromptEditTemplateConfiguration": aws_sdk_qconnect.types.text_full_ai_prompt_edit_template_configuration.serialize_json(
                value["textFullAIPromptEditTemplateConfiguration"]
            )
        }
    else:
        raise SerializationError("AIPromptTemplateConfiguration: no variant present")


def deserialize_json(data: dict) -> AIPromptTemplateConfiguration:
    if "textFullAIPromptEditTemplateConfiguration" in data:
        import aws_sdk_qconnect.types.text_full_ai_prompt_edit_template_configuration

        return {
            "textFullAIPromptEditTemplateConfiguration": aws_sdk_qconnect.types.text_full_ai_prompt_edit_template_configuration.deserialize_json(
                data["textFullAIPromptEditTemplateConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "AIPromptTemplateConfiguration: no recognized variant key"
        )
