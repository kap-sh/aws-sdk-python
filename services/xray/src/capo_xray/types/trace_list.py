"""Generated from Smithy shape ``com.amazonaws.xray#TraceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_xray.types.trace

TraceList: TypeAlias = list["capo_xray.types.trace.Trace"]


# --- restJson1 ser/de ---
def serialize_json(value: TraceList) -> list:
    import capo_xray.types.trace

    out: list = []
    for item in value:
        out.append(capo_xray.types.trace.serialize_json(item))
    return out


def deserialize_json(data: list) -> TraceList:
    import capo_xray.types.trace

    out: TraceList = []
    for item in data:
        out.append(capo_xray.types.trace.deserialize_json(item))
    return out
