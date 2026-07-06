"""Generated from Smithy shape ``com.amazonaws.appsync#UpdateApiCacheResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.api_cache


class UpdateApiCacheResponse(TypedDict, closed=True):
    api_cache: NotRequired["aws_sdk_appsync.types.api_cache.ApiCache"]
    """<p>The <code>ApiCache</code> object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApiCacheResponse) -> dict:
    out: dict = {}
    if "api_cache" in value:
        import aws_sdk_appsync.types.api_cache

        out["apiCache"] = aws_sdk_appsync.types.api_cache.serialize_json(
            value["api_cache"]
        )
    return out


def deserialize_json(data: dict) -> UpdateApiCacheResponse:
    out: UpdateApiCacheResponse = {}  # type: ignore[typeddict-item]
    if "apiCache" in data:
        import aws_sdk_appsync.types.api_cache

        out["api_cache"] = aws_sdk_appsync.types.api_cache.deserialize_json(
            data["apiCache"]
        )
    return out
