"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CollectorsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.collector_short_info_response

CollectorsList: TypeAlias = list[
    "aws_sdk_database_migration_service.types.collector_short_info_response.CollectorShortInfoResponse"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CollectorsList) -> list:
    import aws_sdk_database_migration_service.types.collector_short_info_response

    out: list = []
    for item in value:
        out.append(
            aws_sdk_database_migration_service.types.collector_short_info_response.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CollectorsList:
    import aws_sdk_database_migration_service.types.collector_short_info_response

    out: CollectorsList = []
    for item in data:
        out.append(
            aws_sdk_database_migration_service.types.collector_short_info_response.deserialize_aws_json_1_1(
                item
            )
        )
    return out
