"""Generated from Smithy shape ``com.amazonaws.wellarchitected#MetricType``."""

from typing import Literal, TypeAlias, cast

MetricType: TypeAlias = Literal["WORKLOAD",]


# --- restJson1 ser/de ---
def serialize_json(value: MetricType) -> str:
    return value


def deserialize_json(data: str) -> MetricType:
    return cast(MetricType, data)
