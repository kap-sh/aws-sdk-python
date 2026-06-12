"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.tag_list


class ListTagsForResourceResponse(TypedDict):
    tag_list: NotRequired["aws_sdk_database_migration_service.types.tag_list.TagList"]
    """<p>A list of tags for the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tag_list" in value:
        import aws_sdk_database_migration_service.types.tag_list

        out["TagList"] = (
            aws_sdk_database_migration_service.types.tag_list.serialize_aws_json_1_1(
                value["tag_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "TagList" in data:
        import aws_sdk_database_migration_service.types.tag_list

        out["tag_list"] = (
            aws_sdk_database_migration_service.types.tag_list.deserialize_aws_json_1_1(
                data["TagList"]
            )
        )
    return out
