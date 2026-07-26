"""Generated from Smithy shape ``com.amazonaws.finspace#AutoScalingMetric``."""

from typing import Literal, TypeAlias, cast

AutoScalingMetric: TypeAlias = Literal["CPU_UTILIZATION_PERCENTAGE",]


# --- restJson1 ser/de ---
def serialize_json(value: AutoScalingMetric) -> str:
    return value


def deserialize_json(data: str) -> AutoScalingMetric:
    return cast(AutoScalingMetric, data)
