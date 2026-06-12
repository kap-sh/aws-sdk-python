"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CollectorResponses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.collector_response

CollectorResponses: TypeAlias = list[
    "aws_sdk_database_migration_service.types.collector_response.CollectorResponse"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CollectorResponses) -> list:
    import aws_sdk_database_migration_service.types.collector_response

    out: list = []
    for item in value:
        out.append(
            aws_sdk_database_migration_service.types.collector_response.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CollectorResponses:
    import aws_sdk_database_migration_service.types.collector_response

    out: CollectorResponses = []
    for item in data:
        out.append(
            aws_sdk_database_migration_service.types.collector_response.deserialize_aws_json_1_1(
                item
            )
        )
    return out
