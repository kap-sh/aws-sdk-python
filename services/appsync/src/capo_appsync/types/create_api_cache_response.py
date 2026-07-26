"""Generated from Smithy shape ``com.amazonaws.appsync#CreateApiCacheResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.api_cache


class CreateApiCacheResponse(TypedDict, closed=True):
    api_cache: NotRequired["capo_appsync.types.api_cache.ApiCache"]
    """<p>The <code>ApiCache</code> object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApiCacheResponse) -> dict:
    out: dict = {}
    if "api_cache" in value:
        import capo_appsync.types.api_cache

        out["apiCache"] = capo_appsync.types.api_cache.serialize_json(
            value["api_cache"]
        )
    return out


def deserialize_json(data: dict) -> CreateApiCacheResponse:
    out: CreateApiCacheResponse = {}  # type: ignore[typeddict-item]
    if "apiCache" in data:
        import capo_appsync.types.api_cache

        out["api_cache"] = capo_appsync.types.api_cache.deserialize_json(
            data["apiCache"]
        )
    return out
