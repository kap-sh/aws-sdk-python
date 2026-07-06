"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#Event``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.event_categories_list
    import aws_sdk_database_migration_service.types.source_type
    import aws_sdk_database_migration_service.types.string
    import aws_sdk_database_migration_service.types.t_stamp


class Event(TypedDict, closed=True):
    source_identifier: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p> The identifier of an event source.</p>"""
    source_type: NotRequired[
        "aws_sdk_database_migration_service.types.source_type.SourceType"
    ]
    """<p> The type of DMS resource that generates events. </p> <p>Valid values: replication-instance | endpoint | replication-task</p>"""
    message: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The event message.</p>"""
    event_categories: NotRequired[
        "aws_sdk_database_migration_service.types.event_categories_list.EventCategoriesList"
    ]
    """<p>The event categories available for the specified source type.</p>"""
    date: NotRequired["aws_sdk_database_migration_service.types.t_stamp.TStamp"]
    """<p>The date of the event.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Event) -> dict:
    out: dict = {}
    if "source_identifier" in value:
        out["SourceIdentifier"] = value["source_identifier"]
    if "source_type" in value:
        import aws_sdk_database_migration_service.types.source_type

        out["SourceType"] = (
            aws_sdk_database_migration_service.types.source_type.serialize_aws_json_1_1(
                value["source_type"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "event_categories" in value:
        import aws_sdk_database_migration_service.types.event_categories_list

        out["EventCategories"] = (
            aws_sdk_database_migration_service.types.event_categories_list.serialize_aws_json_1_1(
                value["event_categories"]
            )
        )
    if "date" in value:
        import aws_sdk_database_migration_service.types.t_stamp

        out["Date"] = (
            aws_sdk_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["date"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Event:
    out: Event = {}  # type: ignore[typeddict-item]
    if "SourceIdentifier" in data:
        out["source_identifier"] = data["SourceIdentifier"]
    if "SourceType" in data:
        import aws_sdk_database_migration_service.types.source_type

        out["source_type"] = (
            aws_sdk_database_migration_service.types.source_type.deserialize_aws_json_1_1(
                data["SourceType"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "EventCategories" in data:
        import aws_sdk_database_migration_service.types.event_categories_list

        out["event_categories"] = (
            aws_sdk_database_migration_service.types.event_categories_list.deserialize_aws_json_1_1(
                data["EventCategories"]
            )
        )
    if "Date" in data:
        import aws_sdk_database_migration_service.types.t_stamp

        out["date"] = (
            aws_sdk_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["Date"]
            )
        )
    return out
