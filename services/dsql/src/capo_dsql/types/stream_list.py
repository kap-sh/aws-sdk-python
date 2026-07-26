"""Generated from Smithy shape ``com.amazonaws.dsql#StreamList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dsql.types.stream_summary

StreamList: TypeAlias = list["capo_dsql.types.stream_summary.StreamSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: StreamList) -> list:
    import capo_dsql.types.stream_summary

    out: list = []
    for item in value:
        out.append(capo_dsql.types.stream_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> StreamList:
    import capo_dsql.types.stream_summary

    out: StreamList = []
    for item in data:
        out.append(capo_dsql.types.stream_summary.deserialize_json(item))
    return out
