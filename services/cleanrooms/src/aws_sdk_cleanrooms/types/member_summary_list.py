"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MemberSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.member_summary

MemberSummaryList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.member_summary.MemberSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MemberSummaryList) -> list:
    import aws_sdk_cleanrooms.types.member_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_cleanrooms.types.member_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> MemberSummaryList:
    import aws_sdk_cleanrooms.types.member_summary

    out: MemberSummaryList = []
    for item in data:
        out.append(aws_sdk_cleanrooms.types.member_summary.deserialize_json(item))
    return out
