"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#RunFleetAdvisorLsaAnalysisResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class RunFleetAdvisorLsaAnalysisResponse(TypedDict):
    lsa_analysis_id: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The ID of the LSA analysis run.</p>"""
    status: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The status of the LSA analysis, for example <code>COMPLETED</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RunFleetAdvisorLsaAnalysisResponse) -> dict:
    out: dict = {}
    if "lsa_analysis_id" in value:
        out["LsaAnalysisId"] = value["lsa_analysis_id"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RunFleetAdvisorLsaAnalysisResponse:
    out: RunFleetAdvisorLsaAnalysisResponse = {}  # type: ignore[typeddict-item]
    if "LsaAnalysisId" in data:
        out["lsa_analysis_id"] = data["LsaAnalysisId"]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
