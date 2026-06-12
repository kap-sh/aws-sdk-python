"""Generated from Smithy shape ``com.amazonaws.ivs#StreamSessionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs.types.stream_session_summary

StreamSessionList: TypeAlias = list[
    "aws_sdk_ivs.types.stream_session_summary.StreamSessionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: StreamSessionList) -> list:
    import aws_sdk_ivs.types.stream_session_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_ivs.types.stream_session_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> StreamSessionList:
    import aws_sdk_ivs.types.stream_session_summary

    out: StreamSessionList = []
    for item in data:
        out.append(aws_sdk_ivs.types.stream_session_summary.deserialize_json(item))
    return out
