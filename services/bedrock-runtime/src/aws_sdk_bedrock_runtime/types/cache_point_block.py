"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#CachePointBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.cache_point_type
    import aws_sdk_bedrock_runtime.types.cache_ttl


class CachePointBlock(TypedDict, closed=True):
    type: "aws_sdk_bedrock_runtime.types.cache_point_type.CachePointType"
    """<p>Specifies the type of cache point within the CachePointBlock.</p>"""
    ttl: NotRequired["aws_sdk_bedrock_runtime.types.cache_ttl.CacheTTL"]
    """<p>Optional TTL duration for cache entries. When specified, enables extended TTL caching with the specified duration. When omitted, uses <code>type</code> value for caching behavior.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CachePointBlock) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_runtime.types.cache_point_type

    out["type"] = aws_sdk_bedrock_runtime.types.cache_point_type.serialize_json(
        value["type"]
    )
    if "ttl" in value:
        import aws_sdk_bedrock_runtime.types.cache_ttl

        out["ttl"] = aws_sdk_bedrock_runtime.types.cache_ttl.serialize_json(
            value["ttl"]
        )
    return out


def deserialize_json(data: dict) -> CachePointBlock:
    out: CachePointBlock = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_runtime.types.cache_point_type

        out["type"] = aws_sdk_bedrock_runtime.types.cache_point_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("CachePointBlock.type required")
    if "ttl" in data:
        import aws_sdk_bedrock_runtime.types.cache_ttl

        out["ttl"] = aws_sdk_bedrock_runtime.types.cache_ttl.deserialize_json(
            data["ttl"]
        )
    return out
