"""Generated from Smithy shape ``com.amazonaws.elementalinference#FeedSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elementalinference.types.feed_summary

FeedSummaryList: TypeAlias = list[
    "aws_sdk_elementalinference.types.feed_summary.FeedSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: FeedSummaryList) -> list:
    import aws_sdk_elementalinference.types.feed_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_elementalinference.types.feed_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> FeedSummaryList:
    import aws_sdk_elementalinference.types.feed_summary

    out: FeedSummaryList = []
    for item in data:
        out.append(aws_sdk_elementalinference.types.feed_summary.deserialize_json(item))
    return out
