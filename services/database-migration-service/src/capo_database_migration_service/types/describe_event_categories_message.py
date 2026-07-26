"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeEventCategoriesMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.filter_list
    import capo_database_migration_service.types.string


class DescribeEventCategoriesMessage(TypedDict, closed=True):
    source_type: NotRequired["capo_database_migration_service.types.string.String"]
    """<p> The type of DMS resource that generates events. </p> <p>Valid values: replication-instance | replication-task</p>"""
    filters: NotRequired["capo_database_migration_service.types.filter_list.FilterList"]
    """<p>Filters applied to the event categories.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventCategoriesMessage) -> dict:
    out: dict = {}
    if "source_type" in value:
        out["SourceType"] = value["source_type"]
    if "filters" in value:
        import capo_database_migration_service.types.filter_list

        out["Filters"] = (
            capo_database_migration_service.types.filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventCategoriesMessage:
    out: DescribeEventCategoriesMessage = {}  # type: ignore[typeddict-item]
    if "SourceType" in data:
        out["source_type"] = data["SourceType"]
    if "Filters" in data:
        import capo_database_migration_service.types.filter_list

        out["filters"] = (
            capo_database_migration_service.types.filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    return out
