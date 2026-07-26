"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#BatchStartRecommendationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.start_recommendations_request_entry_list


class BatchStartRecommendationsRequest(TypedDict, closed=True):
    data: NotRequired[
        "capo_database_migration_service.types.start_recommendations_request_entry_list.StartRecommendationsRequestEntryList"
    ]
    """<p>Provides information about source databases to analyze. After this analysis, Fleet Advisor recommends target engines for each source database.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchStartRecommendationsRequest) -> dict:
    out: dict = {}
    if "data" in value:
        import capo_database_migration_service.types.start_recommendations_request_entry_list

        out["Data"] = (
            capo_database_migration_service.types.start_recommendations_request_entry_list.serialize_aws_json_1_1(
                value["data"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchStartRecommendationsRequest:
    out: BatchStartRecommendationsRequest = {}  # type: ignore[typeddict-item]
    if "Data" in data:
        import capo_database_migration_service.types.start_recommendations_request_entry_list

        out["data"] = (
            capo_database_migration_service.types.start_recommendations_request_entry_list.deserialize_aws_json_1_1(
                data["Data"]
            )
        )
    return out
