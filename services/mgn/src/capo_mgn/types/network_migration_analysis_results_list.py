"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationAnalysisResultsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.network_migration_analysis_result

NetworkMigrationAnalysisResultsList: TypeAlias = list[
    "capo_mgn.types.network_migration_analysis_result.NetworkMigrationAnalysisResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationAnalysisResultsList) -> list:
    import capo_mgn.types.network_migration_analysis_result

    out: list = []
    for item in value:
        out.append(
            capo_mgn.types.network_migration_analysis_result.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NetworkMigrationAnalysisResultsList:
    import capo_mgn.types.network_migration_analysis_result

    out: NetworkMigrationAnalysisResultsList = []
    for item in data:
        out.append(
            capo_mgn.types.network_migration_analysis_result.deserialize_json(item)
        )
    return out
