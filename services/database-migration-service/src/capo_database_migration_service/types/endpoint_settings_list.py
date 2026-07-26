"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#EndpointSettingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.endpoint_setting

EndpointSettingsList: TypeAlias = list[
    "capo_database_migration_service.types.endpoint_setting.EndpointSetting"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointSettingsList) -> list:
    import capo_database_migration_service.types.endpoint_setting

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.endpoint_setting.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EndpointSettingsList:
    import capo_database_migration_service.types.endpoint_setting

    out: EndpointSettingsList = []
    for item in data:
        out.append(
            capo_database_migration_service.types.endpoint_setting.deserialize_aws_json_1_1(
                item
            )
        )
    return out
