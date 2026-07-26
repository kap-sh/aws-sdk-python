"""Generated from Smithy shape ``com.amazonaws.iot#StreamsSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.stream_summary

StreamsSummary: TypeAlias = list["capo_iot.types.stream_summary.StreamSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: StreamsSummary) -> list:
    import capo_iot.types.stream_summary

    out: list = []
    for item in value:
        out.append(capo_iot.types.stream_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> StreamsSummary:
    import capo_iot.types.stream_summary

    out: StreamsSummary = []
    for item in data:
        out.append(capo_iot.types.stream_summary.deserialize_json(item))
    return out
