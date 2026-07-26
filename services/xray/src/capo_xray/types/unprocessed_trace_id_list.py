"""Generated from Smithy shape ``com.amazonaws.xray#UnprocessedTraceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_xray.types.trace_id

UnprocessedTraceIdList: TypeAlias = list["capo_xray.types.trace_id.TraceId"]


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedTraceIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> UnprocessedTraceIdList:
    return list(data)
