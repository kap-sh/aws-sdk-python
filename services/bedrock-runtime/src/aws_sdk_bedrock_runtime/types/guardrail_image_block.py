"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailImageBlock``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_image_format
    import aws_sdk_bedrock_runtime.types.guardrail_image_source


class GuardrailImageBlock(TypedDict):
    format: "aws_sdk_bedrock_runtime.types.guardrail_image_format.GuardrailImageFormat"
    """<p>The format details for the file type of the image blocked by the guardrail.</p>"""
    source: "aws_sdk_bedrock_runtime.types.guardrail_image_source.GuardrailImageSource"
    """<p>The image source (image bytes) details of the image blocked by the guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailImageBlock) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_runtime.types.guardrail_image_format

    out["format"] = aws_sdk_bedrock_runtime.types.guardrail_image_format.serialize_json(
        value["format"]
    )
    import aws_sdk_bedrock_runtime.types.guardrail_image_source

    out["source"] = aws_sdk_bedrock_runtime.types.guardrail_image_source.serialize_json(
        value["source"]
    )
    return out


def deserialize_json(data: dict) -> GuardrailImageBlock:
    out: GuardrailImageBlock = {}  # type: ignore[typeddict-item]
    if "format" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_image_format

        out["format"] = (
            aws_sdk_bedrock_runtime.types.guardrail_image_format.deserialize_json(
                data["format"]
            )
        )
    else:
        raise DeserializationError("GuardrailImageBlock.format required")
    if "source" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_image_source

        out["source"] = (
            aws_sdk_bedrock_runtime.types.guardrail_image_source.deserialize_json(
                data["source"]
            )
        )
    else:
        raise DeserializationError("GuardrailImageBlock.source required")
    return out
