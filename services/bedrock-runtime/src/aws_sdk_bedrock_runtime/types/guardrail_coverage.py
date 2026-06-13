"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailCoverage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_image_coverage
    import aws_sdk_bedrock_runtime.types.guardrail_text_characters_coverage


class GuardrailCoverage(TypedDict):
    text_characters: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_text_characters_coverage.GuardrailTextCharactersCoverage"
    ]
    """<p>The text characters of the guardrail coverage details.</p>"""
    images: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_image_coverage.GuardrailImageCoverage"
    ]
    """<p>The guardrail coverage for images (the number of images that guardrails guarded).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailCoverage) -> dict:
    out: dict = {}
    if "text_characters" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_text_characters_coverage

        out["textCharacters"] = (
            aws_sdk_bedrock_runtime.types.guardrail_text_characters_coverage.serialize_json(
                value["text_characters"]
            )
        )
    if "images" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_image_coverage

        out["images"] = (
            aws_sdk_bedrock_runtime.types.guardrail_image_coverage.serialize_json(
                value["images"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailCoverage:
    out: GuardrailCoverage = {}  # type: ignore[typeddict-item]
    if "textCharacters" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_text_characters_coverage

        out["text_characters"] = (
            aws_sdk_bedrock_runtime.types.guardrail_text_characters_coverage.deserialize_json(
                data["textCharacters"]
            )
        )
    if "images" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_image_coverage

        out["images"] = (
            aws_sdk_bedrock_runtime.types.guardrail_image_coverage.deserialize_json(
                data["images"]
            )
        )
    return out
