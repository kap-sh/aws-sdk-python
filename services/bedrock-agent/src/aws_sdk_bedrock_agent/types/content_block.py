"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ContentBlock``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.cache_point_block


class _ContentBlock_text(TypedDict, closed=True):
    text: "str"


class _ContentBlock_cachePoint(TypedDict, closed=True):
    cachePoint: "aws_sdk_bedrock_agent.types.cache_point_block.CachePointBlock"


ContentBlock: TypeAlias = _ContentBlock_text | _ContentBlock_cachePoint


# --- restJson1 ser/de ---
def serialize_json(value: ContentBlock) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    elif "cachePoint" in value:
        import aws_sdk_bedrock_agent.types.cache_point_block

        return {
            "cachePoint": aws_sdk_bedrock_agent.types.cache_point_block.serialize_json(
                value["cachePoint"]
            )
        }
    else:
        raise SerializationError("ContentBlock: no variant present")


def deserialize_json(data: dict) -> ContentBlock:
    if "text" in data:
        return {"text": data["text"]}
    elif "cachePoint" in data:
        import aws_sdk_bedrock_agent.types.cache_point_block

        return {
            "cachePoint": aws_sdk_bedrock_agent.types.cache_point_block.deserialize_json(
                data["cachePoint"]
            )
        }
    else:
        raise DeserializationError("ContentBlock: no recognized variant key")
