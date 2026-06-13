"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#StreamGroupSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gameliftstreams.types.stream_group_summary

StreamGroupSummaryList: TypeAlias = list[
    "aws_sdk_gameliftstreams.types.stream_group_summary.StreamGroupSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: StreamGroupSummaryList) -> list:
    import aws_sdk_gameliftstreams.types.stream_group_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_gameliftstreams.types.stream_group_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> StreamGroupSummaryList:
    import aws_sdk_gameliftstreams.types.stream_group_summary

    out: StreamGroupSummaryList = []
    for item in data:
        out.append(
            aws_sdk_gameliftstreams.types.stream_group_summary.deserialize_json(item)
        )
    return out
