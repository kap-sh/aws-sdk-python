"""Generated from Smithy shape ``com.amazonaws.xray#TraceSpanList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.retrieved_trace

TraceSpanList: TypeAlias = list["aws_sdk_xray.types.retrieved_trace.RetrievedTrace"]


# --- restJson1 ser/de ---
def serialize_json(value: TraceSpanList) -> list:
    import aws_sdk_xray.types.retrieved_trace

    out: list = []
    for item in value:
        out.append(aws_sdk_xray.types.retrieved_trace.serialize_json(item))
    return out


def deserialize_json(data: list) -> TraceSpanList:
    import aws_sdk_xray.types.retrieved_trace

    out: TraceSpanList = []
    for item in data:
        out.append(aws_sdk_xray.types.retrieved_trace.deserialize_json(item))
    return out
