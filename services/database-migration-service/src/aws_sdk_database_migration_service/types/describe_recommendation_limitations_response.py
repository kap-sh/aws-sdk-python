"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeRecommendationLimitationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.limitation_list
    import aws_sdk_database_migration_service.types.string


class DescribeRecommendationLimitationsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The unique pagination token returned for you to pass to a subsequent request. Fleet Advisor returns this token when the number of records in the response is greater than the <code>MaxRecords</code> value. To retrieve the next page, make the call again using the returned token and keeping all other arguments unchanged.</p>"""
    limitations: NotRequired[
        "aws_sdk_database_migration_service.types.limitation_list.LimitationList"
    ]
    """<p>The list of limitations for recommendations of target Amazon Web Services engines.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRecommendationLimitationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limitations" in value:
        import aws_sdk_database_migration_service.types.limitation_list

        out["Limitations"] = (
            aws_sdk_database_migration_service.types.limitation_list.serialize_aws_json_1_1(
                value["limitations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRecommendationLimitationsResponse:
    out: DescribeRecommendationLimitationsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Limitations" in data:
        import aws_sdk_database_migration_service.types.limitation_list

        out["limitations"] = (
            aws_sdk_database_migration_service.types.limitation_list.deserialize_aws_json_1_1(
                data["Limitations"]
            )
        )
    return out
