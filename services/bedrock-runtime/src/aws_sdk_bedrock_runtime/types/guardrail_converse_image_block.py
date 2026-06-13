"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailConverseImageBlock``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_converse_image_format
    import aws_sdk_bedrock_runtime.types.guardrail_converse_image_source


class GuardrailConverseImageBlock(TypedDict):
    format: "aws_sdk_bedrock_runtime.types.guardrail_converse_image_format.GuardrailConverseImageFormat"
    """<p>The format details for the image type of the guardrail converse image block.</p>"""
    source: "aws_sdk_bedrock_runtime.types.guardrail_converse_image_source.GuardrailConverseImageSource"
    """<p>The image source (image bytes) of the guardrail converse image block.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailConverseImageBlock) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_runtime.types.guardrail_converse_image_format

    out["format"] = (
        aws_sdk_bedrock_runtime.types.guardrail_converse_image_format.serialize_json(
            value["format"]
        )
    )
    import aws_sdk_bedrock_runtime.types.guardrail_converse_image_source

    out["source"] = (
        aws_sdk_bedrock_runtime.types.guardrail_converse_image_source.serialize_json(
            value["source"]
        )
    )
    return out


def deserialize_json(data: dict) -> GuardrailConverseImageBlock:
    out: GuardrailConverseImageBlock = {}  # type: ignore[typeddict-item]
    if "format" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_converse_image_format

        out["format"] = (
            aws_sdk_bedrock_runtime.types.guardrail_converse_image_format.deserialize_json(
                data["format"]
            )
        )
    else:
        raise DeserializationError("GuardrailConverseImageBlock.format required")
    if "source" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_converse_image_source

        out["source"] = (
            aws_sdk_bedrock_runtime.types.guardrail_converse_image_source.deserialize_json(
                data["source"]
            )
        )
    else:
        raise DeserializationError("GuardrailConverseImageBlock.source required")
    return out
