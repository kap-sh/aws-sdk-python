"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchPermissionModifications``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.launch_permission_list


class LaunchPermissionModifications(TypedDict, closed=True):
    add: NotRequired["capo_ec2.types.launch_permission_list.LaunchPermissionList"]
    """<p>The Amazon Web Services account ID, organization ARN, or OU ARN to add to the list of launch permissions for the AMI.</p>"""
    remove: NotRequired["capo_ec2.types.launch_permission_list.LaunchPermissionList"]
    """<p>The Amazon Web Services account ID, organization ARN, or OU ARN to remove from the list of launch permissions for the AMI.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchPermissionModifications, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "add" in value:
        import capo_ec2.types.launch_permission_list

        capo_ec2.types.launch_permission_list.serialize_ec2_query(
            value["add"], pairs, f"{key_prefix}Add"
        )
    if "remove" in value:
        import capo_ec2.types.launch_permission_list

        capo_ec2.types.launch_permission_list.serialize_ec2_query(
            value["remove"], pairs, f"{key_prefix}Remove"
        )


def deserialize_ec2_query(el: Element) -> LaunchPermissionModifications:
    out: LaunchPermissionModifications = {}  # type: ignore[typeddict-item]
    if el.find("Add") is not None:
        import capo_ec2.types.launch_permission_list

        out["add"] = capo_ec2.types.launch_permission_list.deserialize_ec2_query(
            el, "Add"
        )
    if el.find("Remove") is not None:
        import capo_ec2.types.launch_permission_list

        out["remove"] = capo_ec2.types.launch_permission_list.deserialize_ec2_query(
            el, "Remove"
        )
    return out
