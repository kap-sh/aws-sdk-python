"""Generated from Smithy shape ``com.amazonaws.mailmanager#SearchSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.search_summary

SearchSummaryList: TypeAlias = list[
    "aws_sdk_mailmanager.types.search_summary.SearchSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SearchSummaryList) -> list:
    import aws_sdk_mailmanager.types.search_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mailmanager.types.search_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SearchSummaryList:
    import aws_sdk_mailmanager.types.search_summary

    out: SearchSummaryList = []
    for item in data:
        out.append(
            aws_sdk_mailmanager.types.search_summary.deserialize_aws_json_1_0(item)
        )
    return out
