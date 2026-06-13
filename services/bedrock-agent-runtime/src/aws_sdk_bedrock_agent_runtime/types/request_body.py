"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RequestBody``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.content_map


class RequestBody(TypedDict):
    content: NotRequired["aws_sdk_bedrock_agent_runtime.types.content_map.ContentMap"]
    """<p>The content in the request body.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RequestBody) -> dict:
    out: dict = {}
    if "content" in value:
        import aws_sdk_bedrock_agent_runtime.types.content_map

        out["content"] = aws_sdk_bedrock_agent_runtime.types.content_map.serialize_json(
            value["content"]
        )
    return out


def deserialize_json(data: dict) -> RequestBody:
    out: RequestBody = {}  # type: ignore[typeddict-item]
    if "content" in data:
        import aws_sdk_bedrock_agent_runtime.types.content_map

        out["content"] = (
            aws_sdk_bedrock_agent_runtime.types.content_map.deserialize_json(
                data["content"]
            )
        )
    return out
