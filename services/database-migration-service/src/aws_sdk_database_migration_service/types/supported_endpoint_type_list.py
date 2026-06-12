"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#SupportedEndpointTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.supported_endpoint_type

SupportedEndpointTypeList: TypeAlias = list[
    "aws_sdk_database_migration_service.types.supported_endpoint_type.SupportedEndpointType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SupportedEndpointTypeList) -> list:
    import aws_sdk_database_migration_service.types.supported_endpoint_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_database_migration_service.types.supported_endpoint_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SupportedEndpointTypeList:
    import aws_sdk_database_migration_service.types.supported_endpoint_type

    out: SupportedEndpointTypeList = []
    for item in data:
        out.append(
            aws_sdk_database_migration_service.types.supported_endpoint_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
