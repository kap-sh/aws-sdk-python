"""Generated from Smithy shape ``com.amazonaws.datazone#UserType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

UserType: TypeAlias = Literal[
    "IAM_USER",
    "IAM_ROLE",
    "SSO_USER",
    "IAM_ROLE_SESSION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IAM_USER",
        "IAM_ROLE",
        "SSO_USER",
        "IAM_ROLE_SESSION",
    )
)


def serialize_json(value: UserType) -> str:
    return value


def deserialize_json(data: str) -> UserType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserType value: {data!r}")
    return cast(UserType, data)
