"""Generated from Smithy shape ``com.amazonaws.elasticache#ModifyUserGroupMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.engine_type
    import aws_sdk_elasticache.types.string
    import aws_sdk_elasticache.types.user_id_list_input


class ModifyUserGroupMessage(TypedDict):
    user_group_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The ID of the user group.</p>"""
    user_ids_to_add: NotRequired[
        "aws_sdk_elasticache.types.user_id_list_input.UserIdListInput"
    ]
    """<p>The list of user IDs to add to the user group.</p>"""
    user_ids_to_remove: NotRequired[
        "aws_sdk_elasticache.types.user_id_list_input.UserIdListInput"
    ]
    """<p>The list of user IDs to remove from the user group.</p>"""
    engine: NotRequired["aws_sdk_elasticache.types.engine_type.EngineType"]
    """<p>Modifies the engine listed in a user group. The options are valkey or redis.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyUserGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "user_group_id" in value:
        pairs.append((f"{prefix}.UserGroupId", str(value["user_group_id"])))
    if "user_ids_to_add" in value:
        import aws_sdk_elasticache.types.user_id_list_input

        aws_sdk_elasticache.types.user_id_list_input.serialize_query(
            value["user_ids_to_add"], pairs, f"{prefix}.UserIdsToAdd"
        )
    if "user_ids_to_remove" in value:
        import aws_sdk_elasticache.types.user_id_list_input

        aws_sdk_elasticache.types.user_id_list_input.serialize_query(
            value["user_ids_to_remove"], pairs, f"{prefix}.UserIdsToRemove"
        )
    if "engine" in value:
        pairs.append((f"{prefix}.Engine", str(value["engine"])))


def deserialize_query(el: Element) -> ModifyUserGroupMessage:
    out: ModifyUserGroupMessage = {}  # type: ignore[typeddict-item]
    child_user_group_id = el.find("UserGroupId")
    if child_user_group_id is not None:
        out["user_group_id"] = str(child_user_group_id.text or "")
    child_user_ids_to_add = el.find("UserIdsToAdd")
    if child_user_ids_to_add is not None:
        import aws_sdk_elasticache.types.user_id_list_input

        out["user_ids_to_add"] = (
            aws_sdk_elasticache.types.user_id_list_input.deserialize_query(
                child_user_ids_to_add
            )
        )
    child_user_ids_to_remove = el.find("UserIdsToRemove")
    if child_user_ids_to_remove is not None:
        import aws_sdk_elasticache.types.user_id_list_input

        out["user_ids_to_remove"] = (
            aws_sdk_elasticache.types.user_id_list_input.deserialize_query(
                child_user_ids_to_remove
            )
        )
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    return out
