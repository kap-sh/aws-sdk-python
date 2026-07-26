"""Generated from Smithy shape ``com.amazonaws.xray#TraceIdListForRetrieval``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_xray.types.trace_id

TraceIdListForRetrieval: TypeAlias = list["capo_xray.types.trace_id.TraceId"]


# --- restJson1 ser/de ---
def serialize_json(value: TraceIdListForRetrieval) -> list:
    return list(value)


def deserialize_json(data: list) -> TraceIdListForRetrieval:
    return list(data)
