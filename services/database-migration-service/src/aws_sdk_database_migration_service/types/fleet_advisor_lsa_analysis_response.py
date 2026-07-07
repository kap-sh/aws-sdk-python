"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#FleetAdvisorLsaAnalysisResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class FleetAdvisorLsaAnalysisResponse(TypedDict, closed=True):
    lsa_analysis_id: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The ID of an LSA analysis run by a Fleet Advisor collector.</p>"""
    status: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The status of an LSA analysis run by a Fleet Advisor collector.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetAdvisorLsaAnalysisResponse) -> dict:
    out: dict = {}
    if "lsa_analysis_id" in value:
        out["LsaAnalysisId"] = value["lsa_analysis_id"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FleetAdvisorLsaAnalysisResponse:
    out: FleetAdvisorLsaAnalysisResponse = {}  # type: ignore[typeddict-item]
    if "LsaAnalysisId" in data:
        out["lsa_analysis_id"] = data["LsaAnalysisId"]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
