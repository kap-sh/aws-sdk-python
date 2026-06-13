"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MembershipSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.membership_summary

MembershipSummaryList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.membership_summary.MembershipSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MembershipSummaryList) -> list:
    import aws_sdk_cleanrooms.types.membership_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_cleanrooms.types.membership_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> MembershipSummaryList:
    import aws_sdk_cleanrooms.types.membership_summary

    out: MembershipSummaryList = []
    for item in data:
        out.append(aws_sdk_cleanrooms.types.membership_summary.deserialize_json(item))
    return out
