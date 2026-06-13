"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailTextBlock``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_content_qualifier_list


class GuardrailTextBlock(TypedDict):
    text: "str"
    """<p>The input text details to be evaluated by the guardrail.</p>"""
    qualifiers: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_content_qualifier_list.GuardrailContentQualifierList"
    ]
    """<p>The qualifiers describing the text block.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTextBlock) -> dict:
    out: dict = {}
    out["text"] = value["text"]
    if "qualifiers" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_content_qualifier_list

        out["qualifiers"] = (
            aws_sdk_bedrock_runtime.types.guardrail_content_qualifier_list.serialize_json(
                value["qualifiers"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailTextBlock:
    out: GuardrailTextBlock = {}  # type: ignore[typeddict-item]
    if "text" in data:
        out["text"] = data["text"]
    else:
        raise DeserializationError("GuardrailTextBlock.text required")
    if "qualifiers" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_content_qualifier_list

        out["qualifiers"] = (
            aws_sdk_bedrock_runtime.types.guardrail_content_qualifier_list.deserialize_json(
                data["qualifiers"]
            )
        )
    return out
