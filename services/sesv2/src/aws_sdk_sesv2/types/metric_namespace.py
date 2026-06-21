"""Generated from Smithy shape ``com.amazonaws.sesv2#MetricNamespace``."""

from typing import Literal, TypeAlias, cast

MetricNamespace: TypeAlias = Literal["VDM",]


# --- restJson1 ser/de ---
def serialize_json(value: MetricNamespace) -> str:
    return value


def deserialize_json(data: str) -> MetricNamespace:
    return cast(MetricNamespace, data)
