"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#SourceDataSettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.source_data_setting

SourceDataSettings: TypeAlias = list[
    "aws_sdk_database_migration_service.types.source_data_setting.SourceDataSetting"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceDataSettings) -> list:
    import aws_sdk_database_migration_service.types.source_data_setting

    out: list = []
    for item in value:
        out.append(
            aws_sdk_database_migration_service.types.source_data_setting.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SourceDataSettings:
    import aws_sdk_database_migration_service.types.source_data_setting

    out: SourceDataSettings = []
    for item in data:
        out.append(
            aws_sdk_database_migration_service.types.source_data_setting.deserialize_aws_json_1_1(
                item
            )
        )
    return out
