"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfAllowListSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.allow_list_summary

__listOfAllowListSummary: TypeAlias = list[
    "aws_sdk_macie2.types.allow_list_summary.AllowListSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAllowListSummary) -> list:
    import aws_sdk_macie2.types.allow_list_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_macie2.types.allow_list_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfAllowListSummary:
    import aws_sdk_macie2.types.allow_list_summary

    out: __listOfAllowListSummary = []
    for item in data:
        out.append(aws_sdk_macie2.types.allow_list_summary.deserialize_json(item))
    return out
