"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.recommendation_list
    import aws_sdk_database_migration_service.types.string


class DescribeRecommendationsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The unique pagination token returned for you to pass to a subsequent request. Fleet Advisor returns this token when the number of records in the response is greater than the <code>MaxRecords</code> value. To retrieve the next page, make the call again using the returned token and keeping all other arguments unchanged.</p>"""
    recommendations: NotRequired[
        "aws_sdk_database_migration_service.types.recommendation_list.RecommendationList"
    ]
    """<p>The list of recommendations of target engines that Fleet Advisor created for the source database.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRecommendationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "recommendations" in value:
        import aws_sdk_database_migration_service.types.recommendation_list

        out["Recommendations"] = (
            aws_sdk_database_migration_service.types.recommendation_list.serialize_aws_json_1_1(
                value["recommendations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRecommendationsResponse:
    out: DescribeRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Recommendations" in data:
        import aws_sdk_database_migration_service.types.recommendation_list

        out["recommendations"] = (
            aws_sdk_database_migration_service.types.recommendation_list.deserialize_aws_json_1_1(
                data["Recommendations"]
            )
        )
    return out
