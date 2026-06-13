"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailConverseTextBlock``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_converse_content_qualifier_list


class GuardrailConverseTextBlock(TypedDict):
    text: "str"
    """<p>The text that you want to guard.</p>"""
    qualifiers: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_converse_content_qualifier_list.GuardrailConverseContentQualifierList"
    ]
    """<p>The qualifier details for the guardrails contextual grounding filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailConverseTextBlock) -> dict:
    out: dict = {}
    out["text"] = value["text"]
    if "qualifiers" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_converse_content_qualifier_list

        out["qualifiers"] = (
            aws_sdk_bedrock_runtime.types.guardrail_converse_content_qualifier_list.serialize_json(
                value["qualifiers"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailConverseTextBlock:
    out: GuardrailConverseTextBlock = {}  # type: ignore[typeddict-item]
    if "text" in data:
        out["text"] = data["text"]
    else:
        raise DeserializationError("GuardrailConverseTextBlock.text required")
    if "qualifiers" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_converse_content_qualifier_list

        out["qualifiers"] = (
            aws_sdk_bedrock_runtime.types.guardrail_converse_content_qualifier_list.deserialize_json(
                data["qualifiers"]
            )
        )
    return out
