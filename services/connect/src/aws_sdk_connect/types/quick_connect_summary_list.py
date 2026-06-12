"""Generated from Smithy shape ``com.amazonaws.connect#QuickConnectSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.quick_connect_summary

QuickConnectSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.quick_connect_summary.QuickConnectSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuickConnectSummaryList) -> list:
    import aws_sdk_connect.types.quick_connect_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.quick_connect_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> QuickConnectSummaryList:
    import aws_sdk_connect.types.quick_connect_summary

    out: QuickConnectSummaryList = []
    for item in data:
        out.append(aws_sdk_connect.types.quick_connect_summary.deserialize_json(item))
    return out
