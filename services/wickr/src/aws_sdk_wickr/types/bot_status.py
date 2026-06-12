"""Generated from Smithy shape ``com.amazonaws.wickr#BotStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wickr.errors import DeserializationError

BotStatus: TypeAlias = Literal[
    1,
    2,
]


# --- restJson1 ser/de ---
_VALUES: frozenset[int] = frozenset(
    (
        1,
        2,
    )
)


def serialize_json(value: BotStatus) -> int:
    return value


def deserialize_json(data: int) -> BotStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BotStatus value: {data!r}")
    return cast(BotStatus, data)
