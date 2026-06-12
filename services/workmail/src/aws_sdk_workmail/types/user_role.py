"""Generated from Smithy shape ``com.amazonaws.workmail#UserRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workmail.errors import DeserializationError

UserRole: TypeAlias = Literal[
    "USER",
    "RESOURCE",
    "SYSTEM_USER",
    "REMOTE_USER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER",
        "RESOURCE",
        "SYSTEM_USER",
        "REMOTE_USER",
    )
)


def serialize_aws_json_1_1(value: UserRole) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserRole:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserRole value: {data!r}")
    return cast(UserRole, data)
