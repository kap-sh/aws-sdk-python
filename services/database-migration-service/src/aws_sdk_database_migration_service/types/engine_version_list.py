"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#EngineVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.engine_version

EngineVersionList: TypeAlias = list[
    "aws_sdk_database_migration_service.types.engine_version.EngineVersion"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EngineVersionList) -> list:
    import aws_sdk_database_migration_service.types.engine_version

    out: list = []
    for item in value:
        out.append(
            aws_sdk_database_migration_service.types.engine_version.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EngineVersionList:
    import aws_sdk_database_migration_service.types.engine_version

    out: EngineVersionList = []
    for item in data:
        out.append(
            aws_sdk_database_migration_service.types.engine_version.deserialize_aws_json_1_1(
                item
            )
        )
    return out
