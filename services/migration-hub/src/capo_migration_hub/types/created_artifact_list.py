"""Generated from Smithy shape ``com.amazonaws.migrationhub#CreatedArtifactList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migration_hub.types.created_artifact

CreatedArtifactList: TypeAlias = list[
    "capo_migration_hub.types.created_artifact.CreatedArtifact"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatedArtifactList) -> list:
    import capo_migration_hub.types.created_artifact

    out: list = []
    for item in value:
        out.append(
            capo_migration_hub.types.created_artifact.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CreatedArtifactList:
    import capo_migration_hub.types.created_artifact

    out: CreatedArtifactList = []
    for item in data:
        out.append(
            capo_migration_hub.types.created_artifact.deserialize_aws_json_1_1(item)
        )
    return out
