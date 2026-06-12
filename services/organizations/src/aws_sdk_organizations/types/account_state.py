"""Generated from Smithy shape ``com.amazonaws.organizations#AccountState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_organizations.errors import DeserializationError

AccountState: TypeAlias = Literal[
    "PENDING_ACTIVATION",
    "ACTIVE",
    "SUSPENDED",
    "PENDING_CLOSURE",
    "CLOSED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_ACTIVATION",
        "ACTIVE",
        "SUSPENDED",
        "PENDING_CLOSURE",
        "CLOSED",
    )
)


def serialize_aws_json_1_1(value: AccountState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccountState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccountState value: {data!r}")
    return cast(AccountState, data)
