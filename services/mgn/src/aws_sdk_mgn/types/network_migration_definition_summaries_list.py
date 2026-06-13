"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationDefinitionSummariesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.network_migration_definition_summary

NetworkMigrationDefinitionSummariesList: TypeAlias = list[
    "aws_sdk_mgn.types.network_migration_definition_summary.NetworkMigrationDefinitionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationDefinitionSummariesList) -> list:
    import aws_sdk_mgn.types.network_migration_definition_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mgn.types.network_migration_definition_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NetworkMigrationDefinitionSummariesList:
    import aws_sdk_mgn.types.network_migration_definition_summary

    out: NetworkMigrationDefinitionSummariesList = []
    for item in data:
        out.append(
            aws_sdk_mgn.types.network_migration_definition_summary.deserialize_json(
                item
            )
        )
    return out
