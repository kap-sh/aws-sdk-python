"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ChangeSpecificationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

ChangeSpecificationType: TypeAlias = Literal[
    "MEMBER",
    "COLLABORATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MEMBER",
        "COLLABORATION",
    )
)


def serialize_json(value: ChangeSpecificationType) -> str:
    return value


def deserialize_json(data: str) -> ChangeSpecificationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChangeSpecificationType value: {data!r}")
    return cast(ChangeSpecificationType, data)
