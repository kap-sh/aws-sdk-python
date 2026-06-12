"""Generated from Smithy shape ``com.amazonaws.gamelift#ComparisonOperatorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

ComparisonOperatorType: TypeAlias = Literal[
    "GreaterThanOrEqualToThreshold",
    "GreaterThanThreshold",
    "LessThanThreshold",
    "LessThanOrEqualToThreshold",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GreaterThanOrEqualToThreshold",
        "GreaterThanThreshold",
        "LessThanThreshold",
        "LessThanOrEqualToThreshold",
    )
)


def serialize_aws_json_1_1(value: ComparisonOperatorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComparisonOperatorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComparisonOperatorType value: {data!r}")
    return cast(ComparisonOperatorType, data)
