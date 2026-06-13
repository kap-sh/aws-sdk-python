"""Generated from Smithy shape ``com.amazonaws.odb#ShapeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

ShapeType: TypeAlias = Literal[
    "AMD",
    "INTEL",
    "INTEL_FLEX_X9",
    "AMPERE_FLEX_A1",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AMD",
        "INTEL",
        "INTEL_FLEX_X9",
        "AMPERE_FLEX_A1",
    )
)


def serialize_aws_json_1_0(value: ShapeType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ShapeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ShapeType value: {data!r}")
    return cast(ShapeType, data)
