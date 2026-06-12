"""Generated from Smithy shape ``com.amazonaws.glue#ListDataQualityStatisticsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.pagination_token
    import aws_sdk_glue.types.statistic_summary_list


class ListDataQualityStatisticsResponse(TypedDict):
    statistics: NotRequired[
        "aws_sdk_glue.types.statistic_summary_list.StatisticSummaryList"
    ]
    """<p>A <code>StatisticSummaryList</code>.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.pagination_token.PaginationToken"]
    """<p>A pagination token to request the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDataQualityStatisticsResponse) -> dict:
    out: dict = {}
    if "statistics" in value:
        import aws_sdk_glue.types.statistic_summary_list

        out["Statistics"] = (
            aws_sdk_glue.types.statistic_summary_list.serialize_aws_json_1_1(
                value["statistics"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDataQualityStatisticsResponse:
    out: ListDataQualityStatisticsResponse = {}  # type: ignore[typeddict-item]
    if "Statistics" in data:
        import aws_sdk_glue.types.statistic_summary_list

        out["statistics"] = (
            aws_sdk_glue.types.statistic_summary_list.deserialize_aws_json_1_1(
                data["Statistics"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
