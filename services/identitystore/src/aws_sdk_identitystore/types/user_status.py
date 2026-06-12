"""Generated from Smithy shape ``com.amazonaws.identitystore#UserStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_identitystore.errors import DeserializationError

UserStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: UserStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserStatus value: {data!r}")
    return cast(UserStatus, data)
