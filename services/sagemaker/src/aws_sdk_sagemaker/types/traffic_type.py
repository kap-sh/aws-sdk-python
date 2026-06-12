"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrafficType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

TrafficType: TypeAlias = Literal[
    "PHASES",
    "STAIRS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PHASES",
        "STAIRS",
    )
)


def serialize_aws_json_1_1(value: TrafficType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrafficType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TrafficType value: {data!r}")
    return cast(TrafficType, data)
