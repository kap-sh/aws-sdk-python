"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationCodeGenerationArtifacts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.network_migration_code_generation_artifact

NetworkMigrationCodeGenerationArtifacts: TypeAlias = list[
    "aws_sdk_mgn.types.network_migration_code_generation_artifact.NetworkMigrationCodeGenerationArtifact"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationCodeGenerationArtifacts) -> list:
    import aws_sdk_mgn.types.network_migration_code_generation_artifact

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mgn.types.network_migration_code_generation_artifact.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> NetworkMigrationCodeGenerationArtifacts:
    import aws_sdk_mgn.types.network_migration_code_generation_artifact

    out: NetworkMigrationCodeGenerationArtifacts = []
    for item in data:
        out.append(
            aws_sdk_mgn.types.network_migration_code_generation_artifact.deserialize_json(
                item
            )
        )
    return out
