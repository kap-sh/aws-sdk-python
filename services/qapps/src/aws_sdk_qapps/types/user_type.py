"""Generated from Smithy shape ``com.amazonaws.qapps#UserType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qapps.errors import DeserializationError

UserType: TypeAlias = Literal[
    "owner",
    "user",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "owner",
        "user",
    )
)


def serialize_json(value: UserType) -> str:
    return value


def deserialize_json(data: str) -> UserType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserType value: {data!r}")
    return cast(UserType, data)
