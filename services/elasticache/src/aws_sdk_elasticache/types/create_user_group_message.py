"""Generated from Smithy shape ``com.amazonaws.elasticache#CreateUserGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.engine_type
    import aws_sdk_elasticache.types.string
    import aws_sdk_elasticache.types.tag_list
    import aws_sdk_elasticache.types.user_id_list_input


class CreateUserGroupMessage(TypedDict, closed=True):
    user_group_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The ID of the user group. This value is stored as a lowercase string.</p>"""
    engine: NotRequired["aws_sdk_elasticache.types.engine_type.EngineType"]
    """<p>Sets the engine listed in a user group. The options are valkey or redis.</p>"""
    user_ids: NotRequired[
        "aws_sdk_elasticache.types.user_id_list_input.UserIdListInput"
    ]
    """<p>The list of user IDs that belong to the user group.</p>"""
    tags: NotRequired["aws_sdk_elasticache.types.tag_list.TagList"]
    """<p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted. Available for Valkey and Redis OSS only.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateUserGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "user_group_id" in value:
        pairs.append((f"{prefix}.UserGroupId", str(value["user_group_id"])))
    if "engine" in value:
        pairs.append((f"{prefix}.Engine", str(value["engine"])))
    if "user_ids" in value:
        import aws_sdk_elasticache.types.user_id_list_input

        aws_sdk_elasticache.types.user_id_list_input.serialize_query(
            value["user_ids"], pairs, f"{prefix}.UserIds"
        )
    if "tags" in value:
        import aws_sdk_elasticache.types.tag_list

        aws_sdk_elasticache.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> CreateUserGroupMessage:
    out: CreateUserGroupMessage = {}  # type: ignore[typeddict-item]
    child_user_group_id = el.find("UserGroupId")
    if child_user_group_id is not None:
        out["user_group_id"] = str(child_user_group_id.text or "")
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_user_ids = el.find("UserIds")
    if child_user_ids is not None:
        import aws_sdk_elasticache.types.user_id_list_input

        out["user_ids"] = (
            aws_sdk_elasticache.types.user_id_list_input.deserialize_query(
                child_user_ids
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_elasticache.types.tag_list

        out["tags"] = aws_sdk_elasticache.types.tag_list.deserialize_query(child_tags)
    return out
