"""Generated from Smithy shape ``com.amazonaws.wisdom#ContentSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.content_summary

ContentSummaryList: TypeAlias = list[
    "aws_sdk_wisdom.types.content_summary.ContentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContentSummaryList) -> list:
    import aws_sdk_wisdom.types.content_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_wisdom.types.content_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContentSummaryList:
    import aws_sdk_wisdom.types.content_summary

    out: ContentSummaryList = []
    for item in data:
        out.append(aws_sdk_wisdom.types.content_summary.deserialize_json(item))
    return out
