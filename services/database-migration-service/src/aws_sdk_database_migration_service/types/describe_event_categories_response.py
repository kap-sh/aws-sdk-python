"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeEventCategoriesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.event_category_group_list


class DescribeEventCategoriesResponse(TypedDict):
    event_category_group_list: NotRequired[
        "aws_sdk_database_migration_service.types.event_category_group_list.EventCategoryGroupList"
    ]
    """<p>A list of event categories.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventCategoriesResponse) -> dict:
    out: dict = {}
    if "event_category_group_list" in value:
        import aws_sdk_database_migration_service.types.event_category_group_list

        out["EventCategoryGroupList"] = (
            aws_sdk_database_migration_service.types.event_category_group_list.serialize_aws_json_1_1(
                value["event_category_group_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventCategoriesResponse:
    out: DescribeEventCategoriesResponse = {}  # type: ignore[typeddict-item]
    if "EventCategoryGroupList" in data:
        import aws_sdk_database_migration_service.types.event_category_group_list

        out["event_category_group_list"] = (
            aws_sdk_database_migration_service.types.event_category_group_list.deserialize_aws_json_1_1(
                data["EventCategoryGroupList"]
            )
        )
    return out
