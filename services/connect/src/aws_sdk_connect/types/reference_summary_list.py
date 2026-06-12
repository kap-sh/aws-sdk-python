"""Generated from Smithy shape ``com.amazonaws.connect#ReferenceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.reference_summary

ReferenceSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.reference_summary.ReferenceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceSummaryList) -> list:
    import aws_sdk_connect.types.reference_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.reference_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReferenceSummaryList:
    import aws_sdk_connect.types.reference_summary

    out: ReferenceSummaryList = []
    for item in data:
        out.append(aws_sdk_connect.types.reference_summary.deserialize_json(item))
    return out
