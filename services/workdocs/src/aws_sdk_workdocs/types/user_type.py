"""Generated from Smithy shape ``com.amazonaws.workdocs#UserType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

UserType: TypeAlias = Literal[
    "USER",
    "ADMIN",
    "POWERUSER",
    "MINIMALUSER",
    "WORKSPACESUSER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER",
        "ADMIN",
        "POWERUSER",
        "MINIMALUSER",
        "WORKSPACESUSER",
    )
)


def serialize_json(value: UserType) -> str:
    return value


def deserialize_json(data: str) -> UserType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserType value: {data!r}")
    return cast(UserType, data)
