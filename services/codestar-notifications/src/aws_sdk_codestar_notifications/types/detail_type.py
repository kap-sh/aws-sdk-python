"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#DetailType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codestar_notifications.errors import DeserializationError

DetailType: TypeAlias = Literal[
    "BASIC",
    "FULL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BASIC",
        "FULL",
    )
)


def serialize_json(value: DetailType) -> str:
    return value


def deserialize_json(data: str) -> DetailType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DetailType value: {data!r}")
    return cast(DetailType, data)
