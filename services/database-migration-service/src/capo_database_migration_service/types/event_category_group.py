"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#EventCategoryGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.event_categories_list
    import capo_database_migration_service.types.string


class EventCategoryGroup(TypedDict, closed=True):
    source_type: NotRequired["capo_database_migration_service.types.string.String"]
    """<p> The type of DMS resource that generates events. </p> <p>Valid values: replication-instance | replication-server | security-group | replication-task</p>"""
    event_categories: NotRequired[
        "capo_database_migration_service.types.event_categories_list.EventCategoriesList"
    ]
    """<p> A list of event categories from a source type that you've chosen.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventCategoryGroup) -> dict:
    out: dict = {}
    if "source_type" in value:
        out["SourceType"] = value["source_type"]
    if "event_categories" in value:
        import capo_database_migration_service.types.event_categories_list

        out["EventCategories"] = (
            capo_database_migration_service.types.event_categories_list.serialize_aws_json_1_1(
                value["event_categories"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EventCategoryGroup:
    out: EventCategoryGroup = {}  # type: ignore[typeddict-item]
    if "SourceType" in data:
        out["source_type"] = data["SourceType"]
    if "EventCategories" in data:
        import capo_database_migration_service.types.event_categories_list

        out["event_categories"] = (
            capo_database_migration_service.types.event_categories_list.deserialize_aws_json_1_1(
                data["EventCategories"]
            )
        )
    return out
