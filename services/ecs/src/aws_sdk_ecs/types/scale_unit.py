"""Generated from Smithy shape ``com.amazonaws.ecs#ScaleUnit``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

ScaleUnit: TypeAlias = Literal["PERCENT",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PERCENT",))


def serialize_aws_json_1_1(value: ScaleUnit) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScaleUnit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScaleUnit value: {data!r}")
    return cast(ScaleUnit, data)
