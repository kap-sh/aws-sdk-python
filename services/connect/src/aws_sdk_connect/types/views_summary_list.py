"""Generated from Smithy shape ``com.amazonaws.connect#ViewsSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.view_summary

ViewsSummaryList: TypeAlias = list["aws_sdk_connect.types.view_summary.ViewSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: ViewsSummaryList) -> list:
    import aws_sdk_connect.types.view_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.view_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ViewsSummaryList:
    import aws_sdk_connect.types.view_summary

    out: ViewsSummaryList = []
    for item in data:
        out.append(aws_sdk_connect.types.view_summary.deserialize_json(item))
    return out
