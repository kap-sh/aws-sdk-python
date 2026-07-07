"""Generated from Smithy shape ``com.amazonaws.appsync#CachingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.caching_keys
    import aws_sdk_appsync.types.long


class CachingConfig(TypedDict, closed=True):
    ttl: "aws_sdk_appsync.types.long.Long"
    """<p>The TTL in seconds for a resolver that has caching activated.</p> <p>Valid values are 1–3,600 seconds.</p>"""
    caching_keys: NotRequired["aws_sdk_appsync.types.caching_keys.CachingKeys"]
    """<p>The caching keys for a resolver that has caching activated.</p> <p>Valid values are entries from the <code>$context.arguments</code>, <code>$context.source</code>, and <code>$context.identity</code> maps.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CachingConfig) -> dict:
    out: dict = {}
    out["ttl"] = value.get("ttl", 0)
    if "caching_keys" in value:
        import aws_sdk_appsync.types.caching_keys

        out["cachingKeys"] = aws_sdk_appsync.types.caching_keys.serialize_json(
            value["caching_keys"]
        )
    return out


def deserialize_json(data: dict) -> CachingConfig:
    out: CachingConfig = {}  # type: ignore[typeddict-item]
    if "ttl" in data:
        out["ttl"] = data["ttl"]
    else:
        out["ttl"] = 0
    if "cachingKeys" in data:
        import aws_sdk_appsync.types.caching_keys

        out["caching_keys"] = aws_sdk_appsync.types.caching_keys.deserialize_json(
            data["cachingKeys"]
        )
    return out
