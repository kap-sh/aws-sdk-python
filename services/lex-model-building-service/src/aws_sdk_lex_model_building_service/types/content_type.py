"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#ContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_model_building_service.errors import DeserializationError

ContentType: TypeAlias = Literal[
    "PlainText",
    "SSML",
    "CustomPayload",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PlainText",
        "SSML",
        "CustomPayload",
    )
)


def serialize_json(value: ContentType) -> str:
    return value


def deserialize_json(data: str) -> ContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContentType value: {data!r}")
    return cast(ContentType, data)
