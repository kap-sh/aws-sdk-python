"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#CacheDetail``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.cache_ttl


class CacheDetail(TypedDict):
    ttl: "aws_sdk_bedrock_runtime.types.cache_ttl.CacheTTL"
    """<p>TTL duration for these cached tokens</p>"""
    input_tokens: "int"
    """<p>Number of tokens written to cache with this TTL (cache creation tokens)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CacheDetail) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_runtime.types.cache_ttl

    out["ttl"] = aws_sdk_bedrock_runtime.types.cache_ttl.serialize_json(value["ttl"])
    out["inputTokens"] = value["input_tokens"]
    return out


def deserialize_json(data: dict) -> CacheDetail:
    out: CacheDetail = {}  # type: ignore[typeddict-item]
    if "ttl" in data:
        import aws_sdk_bedrock_runtime.types.cache_ttl

        out["ttl"] = aws_sdk_bedrock_runtime.types.cache_ttl.deserialize_json(
            data["ttl"]
        )
    else:
        raise DeserializationError("CacheDetail.ttl required")
    if "inputTokens" in data:
        out["input_tokens"] = data["inputTokens"]
    else:
        raise DeserializationError("CacheDetail.input_tokens required")
    return out
