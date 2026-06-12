"""Generated from Smithy shape ``com.amazonaws.finspace#AutoScalingMetric``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace.errors import DeserializationError

AutoScalingMetric: TypeAlias = Literal["CPU_UTILIZATION_PERCENTAGE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CPU_UTILIZATION_PERCENTAGE",))


def serialize_json(value: AutoScalingMetric) -> str:
    return value


def deserialize_json(data: str) -> AutoScalingMetric:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoScalingMetric value: {data!r}")
    return cast(AutoScalingMetric, data)
