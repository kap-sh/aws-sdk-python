"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeFleetAdvisorLsaAnalysisResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.fleet_advisor_lsa_analysis_response_list
    import capo_database_migration_service.types.string


class DescribeFleetAdvisorLsaAnalysisResponse(TypedDict, closed=True):
    analysis: NotRequired[
        "capo_database_migration_service.types.fleet_advisor_lsa_analysis_response_list.FleetAdvisorLsaAnalysisResponseList"
    ]
    """<p>A list of <code>FleetAdvisorLsaAnalysisResponse</code> objects.</p>"""
    next_token: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFleetAdvisorLsaAnalysisResponse) -> dict:
    out: dict = {}
    if "analysis" in value:
        import capo_database_migration_service.types.fleet_advisor_lsa_analysis_response_list

        out["Analysis"] = (
            capo_database_migration_service.types.fleet_advisor_lsa_analysis_response_list.serialize_aws_json_1_1(
                value["analysis"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFleetAdvisorLsaAnalysisResponse:
    out: DescribeFleetAdvisorLsaAnalysisResponse = {}  # type: ignore[typeddict-item]
    if "Analysis" in data:
        import capo_database_migration_service.types.fleet_advisor_lsa_analysis_response_list

        out["analysis"] = (
            capo_database_migration_service.types.fleet_advisor_lsa_analysis_response_list.deserialize_aws_json_1_1(
                data["Analysis"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
