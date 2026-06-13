"""Generated from Smithy shape ``com.amazonaws.freetier#Dimension``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_freetier.errors import DeserializationError

Dimension: TypeAlias = Literal[
    "SERVICE",
    "OPERATION",
    "USAGE_TYPE",
    "REGION",
    "FREE_TIER_TYPE",
    "DESCRIPTION",
    "USAGE_PERCENTAGE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SERVICE",
        "OPERATION",
        "USAGE_TYPE",
        "REGION",
        "FREE_TIER_TYPE",
        "DESCRIPTION",
        "USAGE_PERCENTAGE",
    )
)


def serialize_aws_json_1_0(value: Dimension) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Dimension:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Dimension value: {data!r}")
    return cast(Dimension, data)
