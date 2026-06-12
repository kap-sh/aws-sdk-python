"""Generated from Smithy shape ``com.amazonaws.kinesis#ScalingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis.errors import DeserializationError

ScalingType: TypeAlias = Literal["UNIFORM_SCALING",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("UNIFORM_SCALING",))


def serialize_aws_json_1_1(value: ScalingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScalingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScalingType value: {data!r}")
    return cast(ScalingType, data)
