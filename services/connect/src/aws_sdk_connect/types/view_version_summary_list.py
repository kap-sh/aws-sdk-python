"""Generated from Smithy shape ``com.amazonaws.connect#ViewVersionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.view_version_summary

ViewVersionSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.view_version_summary.ViewVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ViewVersionSummaryList) -> list:
    import aws_sdk_connect.types.view_version_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.view_version_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ViewVersionSummaryList:
    import aws_sdk_connect.types.view_version_summary

    out: ViewVersionSummaryList = []
    for item in data:
        out.append(aws_sdk_connect.types.view_version_summary.deserialize_json(item))
    return out
