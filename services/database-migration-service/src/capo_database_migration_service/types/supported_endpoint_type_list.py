"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#SupportedEndpointTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.supported_endpoint_type

SupportedEndpointTypeList: TypeAlias = list[
    "capo_database_migration_service.types.supported_endpoint_type.SupportedEndpointType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SupportedEndpointTypeList) -> list:
    import capo_database_migration_service.types.supported_endpoint_type

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.supported_endpoint_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SupportedEndpointTypeList:
    import capo_database_migration_service.types.supported_endpoint_type

    out: SupportedEndpointTypeList = []
    for item in data:
        out.append(
            capo_database_migration_service.types.supported_endpoint_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
