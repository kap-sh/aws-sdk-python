"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#FleetAdvisorSchemaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.schema_response

FleetAdvisorSchemaList: TypeAlias = list[
    "capo_database_migration_service.types.schema_response.SchemaResponse"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetAdvisorSchemaList) -> list:
    import capo_database_migration_service.types.schema_response

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.schema_response.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FleetAdvisorSchemaList:
    import capo_database_migration_service.types.schema_response

    out: FleetAdvisorSchemaList = []
    for item in data:
        out.append(
            capo_database_migration_service.types.schema_response.deserialize_aws_json_1_1(
                item
            )
        )
    return out
