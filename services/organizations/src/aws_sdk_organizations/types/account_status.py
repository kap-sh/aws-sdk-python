"""Generated from Smithy shape ``com.amazonaws.organizations#AccountStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_organizations.errors import DeserializationError

AccountStatus: TypeAlias = Literal[
    "ACTIVE",
    "SUSPENDED",
    "PENDING_CLOSURE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "SUSPENDED",
        "PENDING_CLOSURE",
    )
)


def serialize_aws_json_1_1(value: AccountStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccountStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccountStatus value: {data!r}")
    return cast(AccountStatus, data)
