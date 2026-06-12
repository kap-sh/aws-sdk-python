"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

ActionType: TypeAlias = Literal[
    "ADDED_PROFILE_KEY",
    "DELETED_PROFILE_KEY",
    "CREATED",
    "UPDATED",
    "INGESTED",
    "DELETED_BY_CUSTOMER",
    "EXPIRED",
    "MERGED",
    "DELETED_BY_MERGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ADDED_PROFILE_KEY",
        "DELETED_PROFILE_KEY",
        "CREATED",
        "UPDATED",
        "INGESTED",
        "DELETED_BY_CUSTOMER",
        "EXPIRED",
        "MERGED",
        "DELETED_BY_MERGE",
    )
)


def serialize_json(value: ActionType) -> str:
    return value


def deserialize_json(data: str) -> ActionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionType value: {data!r}")
    return cast(ActionType, data)
