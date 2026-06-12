"""Generated from Smithy shape ``com.amazonaws.cloudtrail#SearchSampleQueriesSearchResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.search_sample_queries_search_result

SearchSampleQueriesSearchResults: TypeAlias = list[
    "aws_sdk_cloudtrail.types.search_sample_queries_search_result.SearchSampleQueriesSearchResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchSampleQueriesSearchResults) -> list:
    import aws_sdk_cloudtrail.types.search_sample_queries_search_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudtrail.types.search_sample_queries_search_result.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SearchSampleQueriesSearchResults:
    import aws_sdk_cloudtrail.types.search_sample_queries_search_result

    out: SearchSampleQueriesSearchResults = []
    for item in data:
        out.append(
            aws_sdk_cloudtrail.types.search_sample_queries_search_result.deserialize_aws_json_1_1(
                item
            )
        )
    return out
