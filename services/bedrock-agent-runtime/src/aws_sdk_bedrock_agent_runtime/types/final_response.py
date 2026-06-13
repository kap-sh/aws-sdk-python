"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FinalResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.final_response_string
    import aws_sdk_bedrock_agent_runtime.types.metadata


class FinalResponse(TypedDict):
    text: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.final_response_string.FinalResponseString"
    ]
    """<p>The text in the response to the user.</p>"""
    metadata: NotRequired["aws_sdk_bedrock_agent_runtime.types.metadata.Metadata"]
    """<p>Contains information about the invoke agent operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FinalResponse) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    if "metadata" in value:
        import aws_sdk_bedrock_agent_runtime.types.metadata

        out["metadata"] = aws_sdk_bedrock_agent_runtime.types.metadata.serialize_json(
            value["metadata"]
        )
    return out


def deserialize_json(data: dict) -> FinalResponse:
    out: FinalResponse = {}  # type: ignore[typeddict-item]
    if "text" in data:
        out["text"] = data["text"]
    if "metadata" in data:
        import aws_sdk_bedrock_agent_runtime.types.metadata

        out["metadata"] = aws_sdk_bedrock_agent_runtime.types.metadata.deserialize_json(
            data["metadata"]
        )
    return out
