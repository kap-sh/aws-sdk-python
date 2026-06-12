"""Generated from Smithy shape ``com.amazonaws.lightsail#AccountLevelBpaSyncStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

AccountLevelBpaSyncStatus: TypeAlias = Literal[
    "InSync",
    "Failed",
    "NeverSynced",
    "Defaulted",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InSync",
        "Failed",
        "NeverSynced",
        "Defaulted",
    )
)


def serialize_aws_json_1_1(value: AccountLevelBpaSyncStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccountLevelBpaSyncStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccountLevelBpaSyncStatus value: {data!r}")
    return cast(AccountLevelBpaSyncStatus, data)
