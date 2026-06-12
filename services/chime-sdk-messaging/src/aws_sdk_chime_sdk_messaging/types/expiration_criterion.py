"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ExpirationCriterion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

ExpirationCriterion: TypeAlias = Literal[
    "CREATED_TIMESTAMP",
    "LAST_MESSAGE_TIMESTAMP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED_TIMESTAMP",
        "LAST_MESSAGE_TIMESTAMP",
    )
)


def serialize_json(value: ExpirationCriterion) -> str:
    return value


def deserialize_json(data: str) -> ExpirationCriterion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExpirationCriterion value: {data!r}")
    return cast(ExpirationCriterion, data)
