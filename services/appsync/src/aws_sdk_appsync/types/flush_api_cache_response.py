"""Generated from Smithy shape ``com.amazonaws.appsync#FlushApiCacheResponse``."""

from typing_extensions import TypedDict


class FlushApiCacheResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: FlushApiCacheResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> FlushApiCacheResponse:
    out: FlushApiCacheResponse = {}  # type: ignore[typeddict-item]
    return out
