"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#FleetAdvisorLsaAnalysisResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.fleet_advisor_lsa_analysis_response

FleetAdvisorLsaAnalysisResponseList: TypeAlias = list[
    "aws_sdk_database_migration_service.types.fleet_advisor_lsa_analysis_response.FleetAdvisorLsaAnalysisResponse"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetAdvisorLsaAnalysisResponseList) -> list:
    import aws_sdk_database_migration_service.types.fleet_advisor_lsa_analysis_response

    out: list = []
    for item in value:
        out.append(
            aws_sdk_database_migration_service.types.fleet_advisor_lsa_analysis_response.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FleetAdvisorLsaAnalysisResponseList:
    import aws_sdk_database_migration_service.types.fleet_advisor_lsa_analysis_response

    out: FleetAdvisorLsaAnalysisResponseList = []
    for item in data:
        out.append(
            aws_sdk_database_migration_service.types.fleet_advisor_lsa_analysis_response.deserialize_aws_json_1_1(
                item
            )
        )
    return out
