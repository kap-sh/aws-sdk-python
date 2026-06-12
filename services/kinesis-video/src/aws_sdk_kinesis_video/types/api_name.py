"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#APIName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "PUT_MEDIA",
        "GET_MEDIA",
        "LIST_FRAGMENTS",
        "GET_MEDIA_FOR_FRAGMENT_LIST",
        "GET_HLS_STREAMING_SESSION_URL",
        "GET_DASH_STREAMING_SESSION_URL",
        "GET_CLIP",
        "GET_IMAGES",
    )
)


def serialize_json(value: APIName) -> str:
    return value


def deserialize_json(data: str) -> APIName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown APIName value: {data!r}")
    return cast(APIName, data)
