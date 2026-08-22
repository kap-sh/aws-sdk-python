"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ApiRequestBody``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.api_content_map


class ApiRequestBody(TypedDict, closed=True):
    content: NotRequired[
        "capo_bedrock_agent_runtime.types.api_content_map.ApiContentMap"
    ]
    """<p>The content of the request body. The key of the object in this field is a media type defining the format of the request body.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiRequestBody) -> dict:
    out: dict = {}
    if "content" in value:
        import capo_bedrock_agent_runtime.types.api_content_map

        out["content"] = (
            capo_bedrock_agent_runtime.types.api_content_map.serialize_json(
                value["content"]
            )
        )
    return out


def deserialize_json(data: dict) -> ApiRequestBody:
    out: ApiRequestBody = {}  # type: ignore[typeddict-item]
    if data.get("content") is not None:
        import capo_bedrock_agent_runtime.types.api_content_map

        out["content"] = (
            capo_bedrock_agent_runtime.types.api_content_map.deserialize_json(
                data["content"]
            )
        )
    return out
