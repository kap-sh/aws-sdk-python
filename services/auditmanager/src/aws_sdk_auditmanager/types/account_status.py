"""Generated from Smithy shape ``com.amazonaws.auditmanager#AccountStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auditmanager.errors import DeserializationError

AccountStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
    "PENDING_ACTIVATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
        "PENDING_ACTIVATION",
    )
)


def serialize_json(value: AccountStatus) -> str:
    return value


def deserialize_json(data: str) -> AccountStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccountStatus value: {data!r}")
    return cast(AccountStatus, data)
