"""Generated from Smithy shape ``com.amazonaws.emr#ScalingStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

ScalingStrategy: TypeAlias = Literal[
    "DEFAULT",
    "ADVANCED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT",
        "ADVANCED",
    )
)


def serialize_aws_json_1_1(value: ScalingStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScalingStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScalingStrategy value: {data!r}")
    return cast(ScalingStrategy, data)
