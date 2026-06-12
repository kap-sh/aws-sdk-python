"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#ReferenceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_model_building_service.errors import DeserializationError

ReferenceType: TypeAlias = Literal[
    "Intent",
    "Bot",
    "BotAlias",
    "BotChannel",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Intent",
        "Bot",
        "BotAlias",
        "BotChannel",
    )
)


def serialize_json(value: ReferenceType) -> str:
    return value


def deserialize_json(data: str) -> ReferenceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReferenceType value: {data!r}")
    return cast(ReferenceType, data)
