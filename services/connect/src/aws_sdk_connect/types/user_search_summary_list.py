"""Generated from Smithy shape ``com.amazonaws.connect#UserSearchSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.user_search_summary

UserSearchSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.user_search_summary.UserSearchSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: UserSearchSummaryList) -> list:
    import aws_sdk_connect.types.user_search_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.user_search_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserSearchSummaryList:
    import aws_sdk_connect.types.user_search_summary

    out: UserSearchSummaryList = []
    for item in data:
        out.append(aws_sdk_connect.types.user_search_summary.deserialize_json(item))
    return out
