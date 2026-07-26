"""Generated from Smithy shape ``com.amazonaws.ec2#LoadPermission``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.permission_group
    import capo_ec2.types.string


class LoadPermission(TypedDict, closed=True):
    user_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID.</p>"""
    group: NotRequired["capo_ec2.types.permission_group.PermissionGroup"]
    """<p>The name of the group.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LoadPermission, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "user_id" in value:
        pairs.append((f"{prefix}.UserId", str(value["user_id"])))
    if "group" in value:
        import capo_ec2.types.permission_group

        capo_ec2.types.permission_group.serialize_ec2_query(
            value["group"], pairs, f"{prefix}.Group"
        )


def deserialize_ec2_query(el: Element) -> LoadPermission:
    out: LoadPermission = {}  # type: ignore[typeddict-item]
    child_user_id = el.find("UserId")
    if child_user_id is not None:
        out["user_id"] = str(child_user_id.text or "")
    child_group = el.find("Group")
    if child_group is not None:
        import capo_ec2.types.permission_group

        out["group"] = capo_ec2.types.permission_group.deserialize_ec2_query(
            child_group
        )
    return out
