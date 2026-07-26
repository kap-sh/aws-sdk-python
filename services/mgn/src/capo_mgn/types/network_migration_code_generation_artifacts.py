"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationCodeGenerationArtifacts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.network_migration_code_generation_artifact

NetworkMigrationCodeGenerationArtifacts: TypeAlias = list[
    "capo_mgn.types.network_migration_code_generation_artifact.NetworkMigrationCodeGenerationArtifact"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationCodeGenerationArtifacts) -> list:
    import capo_mgn.types.network_migration_code_generation_artifact

    out: list = []
    for item in value:
        out.append(
            capo_mgn.types.network_migration_code_generation_artifact.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> NetworkMigrationCodeGenerationArtifacts:
    import capo_mgn.types.network_migration_code_generation_artifact

    out: NetworkMigrationCodeGenerationArtifacts = []
    for item in data:
        out.append(
            capo_mgn.types.network_migration_code_generation_artifact.deserialize_json(
                item
            )
        )
    return out
