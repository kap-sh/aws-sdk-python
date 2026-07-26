"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartRecommendationsRequestEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.start_recommendations_request_entry

StartRecommendationsRequestEntryList: TypeAlias = list[
    "capo_database_migration_service.types.start_recommendations_request_entry.StartRecommendationsRequestEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartRecommendationsRequestEntryList) -> list:
    import capo_database_migration_service.types.start_recommendations_request_entry

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.start_recommendations_request_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> StartRecommendationsRequestEntryList:
    import capo_database_migration_service.types.start_recommendations_request_entry

    out: StartRecommendationsRequestEntryList = []
    for item in data:
        out.append(
            capo_database_migration_service.types.start_recommendations_request_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
