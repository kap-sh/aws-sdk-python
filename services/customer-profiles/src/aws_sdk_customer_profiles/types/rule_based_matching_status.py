"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RuleBasedMatchingStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

RuleBasedMatchingStatus: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "ACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "IN_PROGRESS",
        "ACTIVE",
    )
)


def serialize_json(value: RuleBasedMatchingStatus) -> str:
    return value


def deserialize_json(data: str) -> RuleBasedMatchingStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleBasedMatchingStatus value: {data!r}")
    return cast(RuleBasedMatchingStatus, data)
