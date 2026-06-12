"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#BatchStartRecommendationsErrorEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.batch_start_recommendations_error_entry

BatchStartRecommendationsErrorEntryList: TypeAlias = list[
    "aws_sdk_database_migration_service.types.batch_start_recommendations_error_entry.BatchStartRecommendationsErrorEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchStartRecommendationsErrorEntryList) -> list:
    import aws_sdk_database_migration_service.types.batch_start_recommendations_error_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_database_migration_service.types.batch_start_recommendations_error_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchStartRecommendationsErrorEntryList:
    import aws_sdk_database_migration_service.types.batch_start_recommendations_error_entry

    out: BatchStartRecommendationsErrorEntryList = []
    for item in data:
        out.append(
            aws_sdk_database_migration_service.types.batch_start_recommendations_error_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
