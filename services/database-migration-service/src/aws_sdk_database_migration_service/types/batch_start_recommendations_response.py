"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#BatchStartRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.batch_start_recommendations_error_entry_list


class BatchStartRecommendationsResponse(TypedDict, closed=True):
    error_entries: NotRequired[
        "aws_sdk_database_migration_service.types.batch_start_recommendations_error_entry_list.BatchStartRecommendationsErrorEntryList"
    ]
    """<p>A list with error details about the analysis of each source database.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchStartRecommendationsResponse) -> dict:
    out: dict = {}
    if "error_entries" in value:
        import aws_sdk_database_migration_service.types.batch_start_recommendations_error_entry_list

        out["ErrorEntries"] = (
            aws_sdk_database_migration_service.types.batch_start_recommendations_error_entry_list.serialize_aws_json_1_1(
                value["error_entries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchStartRecommendationsResponse:
    out: BatchStartRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if "ErrorEntries" in data:
        import aws_sdk_database_migration_service.types.batch_start_recommendations_error_entry_list

        out["error_entries"] = (
            aws_sdk_database_migration_service.types.batch_start_recommendations_error_entry_list.deserialize_aws_json_1_1(
                data["ErrorEntries"]
            )
        )
    return out
