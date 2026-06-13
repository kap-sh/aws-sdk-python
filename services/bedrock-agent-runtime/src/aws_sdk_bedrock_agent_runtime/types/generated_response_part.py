"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GeneratedResponsePart``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.text_response_part


class GeneratedResponsePart(TypedDict):
    text_response_part: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.text_response_part.TextResponsePart"
    ]
    """<p>Contains metadata about a textual part of the generated response that is accompanied by a citation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeneratedResponsePart) -> dict:
    out: dict = {}
    if "text_response_part" in value:
        import aws_sdk_bedrock_agent_runtime.types.text_response_part

        out["textResponsePart"] = (
            aws_sdk_bedrock_agent_runtime.types.text_response_part.serialize_json(
                value["text_response_part"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeneratedResponsePart:
    out: GeneratedResponsePart = {}  # type: ignore[typeddict-item]
    if "textResponsePart" in data:
        import aws_sdk_bedrock_agent_runtime.types.text_response_part

        out["text_response_part"] = (
            aws_sdk_bedrock_agent_runtime.types.text_response_part.deserialize_json(
                data["textResponsePart"]
            )
        )
    return out
