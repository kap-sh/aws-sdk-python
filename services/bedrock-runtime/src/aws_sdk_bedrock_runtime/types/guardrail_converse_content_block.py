"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailConverseContentBlock``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_converse_image_block
    import aws_sdk_bedrock_runtime.types.guardrail_converse_text_block


class _GuardrailConverseContentBlock_text(TypedDict, closed=True):
    text: "aws_sdk_bedrock_runtime.types.guardrail_converse_text_block.GuardrailConverseTextBlock"


class _GuardrailConverseContentBlock_image(TypedDict, closed=True):
    image: "aws_sdk_bedrock_runtime.types.guardrail_converse_image_block.GuardrailConverseImageBlock"


GuardrailConverseContentBlock: TypeAlias = (
    _GuardrailConverseContentBlock_text | _GuardrailConverseContentBlock_image
)


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailConverseContentBlock) -> dict:
    if "text" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_converse_text_block

        return {
            "text": aws_sdk_bedrock_runtime.types.guardrail_converse_text_block.serialize_json(
                value["text"]
            )
        }
    elif "image" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_converse_image_block

        return {
            "image": aws_sdk_bedrock_runtime.types.guardrail_converse_image_block.serialize_json(
                value["image"]
            )
        }
    else:
        raise SerializationError("GuardrailConverseContentBlock: no variant present")


def deserialize_json(data: dict) -> GuardrailConverseContentBlock:
    if "text" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_converse_text_block

        return {
            "text": aws_sdk_bedrock_runtime.types.guardrail_converse_text_block.deserialize_json(
                data["text"]
            )
        }
    elif "image" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_converse_image_block

        return {
            "image": aws_sdk_bedrock_runtime.types.guardrail_converse_image_block.deserialize_json(
                data["image"]
            )
        }
    else:
        raise DeserializationError(
            "GuardrailConverseContentBlock: no recognized variant key"
        )
