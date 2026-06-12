"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CachePointBlock``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.cache_point_type


class CachePointBlock(TypedDict):
    type: "aws_sdk_bedrock_agent.types.cache_point_type.CachePointType"
    """<p>Indicates that the CachePointBlock is of the default type</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CachePointBlock) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.cache_point_type

    out["type"] = aws_sdk_bedrock_agent.types.cache_point_type.serialize_json(
        value["type"]
    )
    return out


def deserialize_json(data: dict) -> CachePointBlock:
    out: CachePointBlock = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_agent.types.cache_point_type

        out["type"] = aws_sdk_bedrock_agent.types.cache_point_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("CachePointBlock.type required")
    return out
