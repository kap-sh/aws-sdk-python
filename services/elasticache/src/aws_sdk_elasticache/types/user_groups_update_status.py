"""Generated from Smithy shape ``com.amazonaws.elasticache#UserGroupsUpdateStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.user_group_id_list


class UserGroupsUpdateStatus(TypedDict):
    user_group_ids_to_add: NotRequired[
        "aws_sdk_elasticache.types.user_group_id_list.UserGroupIdList"
    ]
    """<p>The ID of the user group to add.</p>"""
    user_group_ids_to_remove: NotRequired[
        "aws_sdk_elasticache.types.user_group_id_list.UserGroupIdList"
    ]
    """<p>The ID of the user group to remove.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UserGroupsUpdateStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "user_group_ids_to_add" in value:
        import aws_sdk_elasticache.types.user_group_id_list

        aws_sdk_elasticache.types.user_group_id_list.serialize_query(
            value["user_group_ids_to_add"], pairs, f"{prefix}.UserGroupIdsToAdd"
        )
    if "user_group_ids_to_remove" in value:
        import aws_sdk_elasticache.types.user_group_id_list

        aws_sdk_elasticache.types.user_group_id_list.serialize_query(
            value["user_group_ids_to_remove"], pairs, f"{prefix}.UserGroupIdsToRemove"
        )


def deserialize_query(el: Element) -> UserGroupsUpdateStatus:
    out: UserGroupsUpdateStatus = {}  # type: ignore[typeddict-item]
    child_user_group_ids_to_add = el.find("UserGroupIdsToAdd")
    if child_user_group_ids_to_add is not None:
        import aws_sdk_elasticache.types.user_group_id_list

        out["user_group_ids_to_add"] = (
            aws_sdk_elasticache.types.user_group_id_list.deserialize_query(
                child_user_group_ids_to_add
            )
        )
    child_user_group_ids_to_remove = el.find("UserGroupIdsToRemove")
    if child_user_group_ids_to_remove is not None:
        import aws_sdk_elasticache.types.user_group_id_list

        out["user_group_ids_to_remove"] = (
            aws_sdk_elasticache.types.user_group_id_list.deserialize_query(
                child_user_group_ids_to_remove
            )
        )
    return out
