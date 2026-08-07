"""Generated from Smithy shape ``com.amazonaws.elasticache#UserGroupPendingChanges``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.user_id_list


class UserGroupPendingChanges(TypedDict, closed=True):
    user_ids_to_remove: NotRequired["capo_elasticache.types.user_id_list.UserIdList"]
    """<p>The list of user IDs to remove.</p>"""
    user_ids_to_add: NotRequired["capo_elasticache.types.user_id_list.UserIdList"]
    """<p>The list of user IDs to add.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UserGroupPendingChanges, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "user_ids_to_remove" in value:
        import capo_elasticache.types.user_id_list

        capo_elasticache.types.user_id_list.serialize_query(
            value["user_ids_to_remove"], pairs, f"{key_prefix}UserIdsToRemove"
        )
    if "user_ids_to_add" in value:
        import capo_elasticache.types.user_id_list

        capo_elasticache.types.user_id_list.serialize_query(
            value["user_ids_to_add"], pairs, f"{key_prefix}UserIdsToAdd"
        )


def deserialize_query(el: Element) -> UserGroupPendingChanges:
    out: UserGroupPendingChanges = {}  # type: ignore[typeddict-item]
    child_user_ids_to_remove = el.find("UserIdsToRemove")
    if child_user_ids_to_remove is not None:
        import capo_elasticache.types.user_id_list

        out["user_ids_to_remove"] = (
            capo_elasticache.types.user_id_list.deserialize_query(
                child_user_ids_to_remove
            )
        )
    child_user_ids_to_add = el.find("UserIdsToAdd")
    if child_user_ids_to_add is not None:
        import capo_elasticache.types.user_id_list

        out["user_ids_to_add"] = capo_elasticache.types.user_id_list.deserialize_query(
            child_user_ids_to_add
        )
    return out
