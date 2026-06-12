"""Generated from Smithy shape ``com.amazonaws.xray#Histogram``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.histogram_entry

Histogram: TypeAlias = list["aws_sdk_xray.types.histogram_entry.HistogramEntry"]


# --- restJson1 ser/de ---
def serialize_json(value: Histogram) -> list:
    import aws_sdk_xray.types.histogram_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_xray.types.histogram_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> Histogram:
    import aws_sdk_xray.types.histogram_entry

    out: Histogram = []
    for item in data:
        out.append(aws_sdk_xray.types.histogram_entry.deserialize_json(item))
    return out
