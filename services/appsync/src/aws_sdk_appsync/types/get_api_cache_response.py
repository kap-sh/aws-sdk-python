"""Generated from Smithy shape ``com.amazonaws.appsync#GetApiCacheResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.api_cache


class GetApiCacheResponse(TypedDict):
    api_cache: NotRequired["aws_sdk_appsync.types.api_cache.ApiCache"]
    """<p>The <code>ApiCache</code> object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApiCacheResponse) -> dict:
    out: dict = {}
    if "api_cache" in value:
        import aws_sdk_appsync.types.api_cache

        out["apiCache"] = aws_sdk_appsync.types.api_cache.serialize_json(
            value["api_cache"]
        )
    return out


def deserialize_json(data: dict) -> GetApiCacheResponse:
    out: GetApiCacheResponse = {}  # type: ignore[typeddict-item]
    if "apiCache" in data:
        import aws_sdk_appsync.types.api_cache

        out["api_cache"] = aws_sdk_appsync.types.api_cache.deserialize_json(
            data["apiCache"]
        )
    return out
