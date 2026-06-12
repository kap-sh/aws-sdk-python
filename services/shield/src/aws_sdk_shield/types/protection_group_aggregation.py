"""Generated from Smithy shape ``com.amazonaws.shield#ProtectionGroupAggregation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_shield.errors import DeserializationError

ProtectionGroupAggregation: TypeAlias = Literal[
    "SUM",
    "MEAN",
    "MAX",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUM",
        "MEAN",
        "MAX",
    )
)


def serialize_aws_json_1_1(value: ProtectionGroupAggregation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProtectionGroupAggregation:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ProtectionGroupAggregation value: {data!r}"
        )
    return cast(ProtectionGroupAggregation, data)
