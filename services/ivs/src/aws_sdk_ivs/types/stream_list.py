"""Generated from Smithy shape ``com.amazonaws.ivs#StreamList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs.types.stream_summary

StreamList: TypeAlias = list["aws_sdk_ivs.types.stream_summary.StreamSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: StreamList) -> list:
    import aws_sdk_ivs.types.stream_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_ivs.types.stream_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> StreamList:
    import aws_sdk_ivs.types.stream_summary

    out: StreamList = []
    for item in data:
        out.append(aws_sdk_ivs.types.stream_summary.deserialize_json(item))
    return out
