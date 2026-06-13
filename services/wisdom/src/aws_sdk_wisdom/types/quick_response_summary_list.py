"""Generated from Smithy shape ``com.amazonaws.wisdom#QuickResponseSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.quick_response_summary

QuickResponseSummaryList: TypeAlias = list[
    "aws_sdk_wisdom.types.quick_response_summary.QuickResponseSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuickResponseSummaryList) -> list:
    import aws_sdk_wisdom.types.quick_response_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_wisdom.types.quick_response_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> QuickResponseSummaryList:
    import aws_sdk_wisdom.types.quick_response_summary

    out: QuickResponseSummaryList = []
    for item in data:
        out.append(aws_sdk_wisdom.types.quick_response_summary.deserialize_json(item))
    return out
