"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeFleetAdvisorLsaAnalysisRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.string


class DescribeFleetAdvisorLsaAnalysisRequest(TypedDict, closed=True):
    max_records: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Sets the maximum number of records returned in the response.</p>"""
    next_token: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>If <code>NextToken</code> is returned by a previous response, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFleetAdvisorLsaAnalysisRequest) -> dict:
    out: dict = {}
    if "max_records" in value:
        out["MaxRecords"] = value["max_records"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFleetAdvisorLsaAnalysisRequest:
    out: DescribeFleetAdvisorLsaAnalysisRequest = {}  # type: ignore[typeddict-item]
    if "MaxRecords" in data:
        out["max_records"] = data["MaxRecords"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
