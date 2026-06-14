"""Generated from Smithy shape ``com.amazonaws.datazone#UserSearchType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

UserSearchType: TypeAlias = Literal[
    "SSO_USER",
    "DATAZONE_USER",
    "DATAZONE_SSO_USER",
    "DATAZONE_IAM_USER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SSO_USER",
        "DATAZONE_USER",
        "DATAZONE_SSO_USER",
        "DATAZONE_IAM_USER",
    )
)


def serialize_json(value: UserSearchType) -> str:
    return value


def deserialize_json(data: str) -> UserSearchType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserSearchType value: {data!r}")
    return cast(UserSearchType, data)
