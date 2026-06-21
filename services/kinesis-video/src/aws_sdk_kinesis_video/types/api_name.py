"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#APIName``."""

from typing import Literal, TypeAlias, cast

APIName: TypeAlias = Literal[
    "PUT_MEDIA",
    "GET_MEDIA",
    "LIST_FRAGMENTS",
    "GET_MEDIA_FOR_FRAGMENT_LIST",
    "GET_HLS_STREAMING_SESSION_URL",
    "GET_DASH_STREAMING_SESSION_URL",
    "GET_CLIP",
    "GET_IMAGES",
]


# --- restJson1 ser/de ---
def serialize_json(value: APIName) -> str:
    return value


def deserialize_json(data: str) -> APIName:
    return cast(APIName, data)
