"""Generated from Smithy shape ``com.amazonaws.pi#ListPerformanceAnalysisReportRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pi.types.next_token
    import aws_sdk_pi.types.recommendation_list


class ListPerformanceAnalysisReportRecommendationsResponse(TypedDict, closed=True):
    recommendations: NotRequired[
        "aws_sdk_pi.types.recommendation_list.RecommendationList"
    ]
    """<p>The list of recommendations for the analysis report.</p>"""
    next_token: NotRequired["aws_sdk_pi.types.next_token.NextToken"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by <code>MaxResults</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListPerformanceAnalysisReportRecommendationsResponse,
) -> dict:
    out: dict = {}
    if "recommendations" in value:
        import aws_sdk_pi.types.recommendation_list

        out["Recommendations"] = (
            aws_sdk_pi.types.recommendation_list.serialize_aws_json_1_1(
                value["recommendations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListPerformanceAnalysisReportRecommendationsResponse:
    out: ListPerformanceAnalysisReportRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if "Recommendations" in data:
        import aws_sdk_pi.types.recommendation_list

        out["recommendations"] = (
            aws_sdk_pi.types.recommendation_list.deserialize_aws_json_1_1(
                data["Recommendations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
