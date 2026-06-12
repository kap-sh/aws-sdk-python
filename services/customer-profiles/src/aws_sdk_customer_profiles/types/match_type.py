"""Generated from Smithy shape ``com.amazonaws.customerprofiles#MatchType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

MatchType: TypeAlias = Literal[
    "RULE_BASED_MATCHING",
    "ML_BASED_MATCHING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RULE_BASED_MATCHING",
        "ML_BASED_MATCHING",
    )
)


def serialize_json(value: MatchType) -> str:
    return value


def deserialize_json(data: str) -> MatchType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MatchType value: {data!r}")
    return cast(MatchType, data)
