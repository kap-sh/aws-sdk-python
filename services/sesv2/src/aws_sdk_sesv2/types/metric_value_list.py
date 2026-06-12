"""Generated from Smithy shape ``com.amazonaws.sesv2#MetricValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.counter

MetricValueList: TypeAlias = list["aws_sdk_sesv2.types.counter.Counter"]


# --- restJson1 ser/de ---
def serialize_json(value: MetricValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> MetricValueList:
    return list(data)
