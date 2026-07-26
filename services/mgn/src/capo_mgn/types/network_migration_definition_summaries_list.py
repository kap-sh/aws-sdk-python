"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationDefinitionSummariesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.network_migration_definition_summary

NetworkMigrationDefinitionSummariesList: TypeAlias = list[
    "capo_mgn.types.network_migration_definition_summary.NetworkMigrationDefinitionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationDefinitionSummariesList) -> list:
    import capo_mgn.types.network_migration_definition_summary

    out: list = []
    for item in value:
        out.append(
            capo_mgn.types.network_migration_definition_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NetworkMigrationDefinitionSummariesList:
    import capo_mgn.types.network_migration_definition_summary

    out: NetworkMigrationDefinitionSummariesList = []
    for item in data:
        out.append(
            capo_mgn.types.network_migration_definition_summary.deserialize_json(item)
        )
    return out
