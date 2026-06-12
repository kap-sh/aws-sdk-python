"""Generated from Smithy shape ``com.amazonaws.xray#TraceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.trace_id

TraceIdList: TypeAlias = list["aws_sdk_xray.types.trace_id.TraceId"]


# --- restJson1 ser/de ---
def serialize_json(value: TraceIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> TraceIdList:
    return list(data)
