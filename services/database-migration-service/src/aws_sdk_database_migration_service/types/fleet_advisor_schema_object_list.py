"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#FleetAdvisorSchemaObjectList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.fleet_advisor_schema_object_response

FleetAdvisorSchemaObjectList: TypeAlias = list[
    "aws_sdk_database_migration_service.types.fleet_advisor_schema_object_response.FleetAdvisorSchemaObjectResponse"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetAdvisorSchemaObjectList) -> list:
    import aws_sdk_database_migration_service.types.fleet_advisor_schema_object_response

    out: list = []
    for item in value:
        out.append(
            aws_sdk_database_migration_service.types.fleet_advisor_schema_object_response.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FleetAdvisorSchemaObjectList:
    import aws_sdk_database_migration_service.types.fleet_advisor_schema_object_response

    out: FleetAdvisorSchemaObjectList = []
    for item in data:
        out.append(
            aws_sdk_database_migration_service.types.fleet_advisor_schema_object_response.deserialize_aws_json_1_1(
                item
            )
        )
    return out
