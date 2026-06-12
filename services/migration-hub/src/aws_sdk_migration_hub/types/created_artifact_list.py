"""Generated from Smithy shape ``com.amazonaws.migrationhub#CreatedArtifactList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migration_hub.types.created_artifact

CreatedArtifactList: TypeAlias = list[
    "aws_sdk_migration_hub.types.created_artifact.CreatedArtifact"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatedArtifactList) -> list:
    import aws_sdk_migration_hub.types.created_artifact

    out: list = []
    for item in value:
        out.append(
            aws_sdk_migration_hub.types.created_artifact.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CreatedArtifactList:
    import aws_sdk_migration_hub.types.created_artifact

    out: CreatedArtifactList = []
    for item in data:
        out.append(
            aws_sdk_migration_hub.types.created_artifact.deserialize_aws_json_1_1(item)
        )
    return out
