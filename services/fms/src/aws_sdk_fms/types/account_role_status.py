"""Generated from Smithy shape ``com.amazonaws.fms#AccountRoleStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fms.errors import DeserializationError

AccountRoleStatus: TypeAlias = Literal[
    "READY",
    "CREATING",
    "PENDING_DELETION",
    "DELETING",
    "DELETED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READY",
        "CREATING",
        "PENDING_DELETION",
        "DELETING",
        "DELETED",
    )
)


def serialize_aws_json_1_1(value: AccountRoleStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccountRoleStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccountRoleStatus value: {data!r}")
    return cast(AccountRoleStatus, data)
