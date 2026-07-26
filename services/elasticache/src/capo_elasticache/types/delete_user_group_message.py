"""Generated from Smithy shape ``com.amazonaws.elasticache#DeleteUserGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string


class DeleteUserGroupMessage(TypedDict, closed=True):
    user_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The ID of the user group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteUserGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "user_group_id" in value:
        pairs.append((f"{prefix}.UserGroupId", str(value["user_group_id"])))


def deserialize_query(el: Element) -> DeleteUserGroupMessage:
    out: DeleteUserGroupMessage = {}  # type: ignore[typeddict-item]
    child_user_group_id = el.find("UserGroupId")
    if child_user_group_id is not None:
        out["user_group_id"] = str(child_user_group_id.text or "")
    return out
