"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tag_list: NotRequired["capo_database_migration_service.types.tag_list.TagList"]
    """<p>A list of tags for the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tag_list" in value:
        import capo_database_migration_service.types.tag_list

        out["TagList"] = (
            capo_database_migration_service.types.tag_list.serialize_aws_json_1_1(
                value["tag_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "TagList" in data:
        import capo_database_migration_service.types.tag_list

        out["tag_list"] = (
            capo_database_migration_service.types.tag_list.deserialize_aws_json_1_1(
                data["TagList"]
            )
        )
    return out
