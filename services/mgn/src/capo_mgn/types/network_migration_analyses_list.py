"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationAnalysesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.network_migration_analysis_job_details

NetworkMigrationAnalysesList: TypeAlias = list[
    "capo_mgn.types.network_migration_analysis_job_details.NetworkMigrationAnalysisJobDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationAnalysesList) -> list:
    import capo_mgn.types.network_migration_analysis_job_details

    out: list = []
    for item in value:
        out.append(
            capo_mgn.types.network_migration_analysis_job_details.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NetworkMigrationAnalysesList:
    import capo_mgn.types.network_migration_analysis_job_details

    out: NetworkMigrationAnalysesList = []
    for item in data:
        out.append(
            capo_mgn.types.network_migration_analysis_job_details.deserialize_json(item)
        )
    return out
