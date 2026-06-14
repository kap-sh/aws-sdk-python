"""Generated from Smithy shape ``com.amazonaws.datazone#UserProfileType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

UserProfileType: TypeAlias = Literal[
    "IAM",
    "SSO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IAM",
        "SSO",
    )
)


def serialize_json(value: UserProfileType) -> str:
    return value


def deserialize_json(data: str) -> UserProfileType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserProfileType value: {data!r}")
    return cast(UserProfileType, data)
