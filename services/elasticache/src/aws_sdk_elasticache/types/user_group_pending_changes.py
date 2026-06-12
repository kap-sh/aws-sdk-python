"""Generated from Smithy shape ``com.amazonaws.elasticache#UserGroupPendingChanges``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.user_id_list


class UserGroupPendingChanges(TypedDict):
    user_ids_to_remove: NotRequired["aws_sdk_elasticache.types.user_id_list.UserIdList"]
    """<p>The list of user IDs to remove.</p>"""
    user_ids_to_add: NotRequired["aws_sdk_elasticache.types.user_id_list.UserIdList"]
    """<p>The list of user IDs to add.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UserGroupPendingChanges, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "user_ids_to_remove" in value:
        import aws_sdk_elasticache.types.user_id_list

        aws_sdk_elasticache.types.user_id_list.serialize_query(
            value["user_ids_to_remove"], pairs, f"{prefix}.UserIdsToRemove"
        )
    if "user_ids_to_add" in value:
        import aws_sdk_elasticache.types.user_id_list

        aws_sdk_elasticache.types.user_id_list.serialize_query(
            value["user_ids_to_add"], pairs, f"{prefix}.UserIdsToAdd"
        )


def deserialize_query(el: Element) -> UserGroupPendingChanges:
    out: UserGroupPendingChanges = {}  # type: ignore[typeddict-item]
    child_user_ids_to_remove = el.find("UserIdsToRemove")
    if child_user_ids_to_remove is not None:
        import aws_sdk_elasticache.types.user_id_list

        out["user_ids_to_remove"] = (
            aws_sdk_elasticache.types.user_id_list.deserialize_query(
                child_user_ids_to_remove
            )
        )
    child_user_ids_to_add = el.find("UserIdsToAdd")
    if child_user_ids_to_add is not None:
        import aws_sdk_elasticache.types.user_id_list

        out["user_ids_to_add"] = (
            aws_sdk_elasticache.types.user_id_list.deserialize_query(
                child_user_ids_to_add
            )
        )
    return out
