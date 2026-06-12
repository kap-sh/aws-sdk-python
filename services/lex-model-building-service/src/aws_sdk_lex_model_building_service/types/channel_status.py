"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#ChannelStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_model_building_service.errors import DeserializationError

ChannelStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "CREATED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "CREATED",
        "FAILED",
    )
)


def serialize_json(value: ChannelStatus) -> str:
    return value


def deserialize_json(data: str) -> ChannelStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChannelStatus value: {data!r}")
    return cast(ChannelStatus, data)
