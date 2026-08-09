"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVolumePermissionModifications``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.create_volume_permission_list


class CreateVolumePermissionModifications(TypedDict, closed=True):
    add: NotRequired[
        "capo_ec2.types.create_volume_permission_list.CreateVolumePermissionList"
    ]
    """<p>Adds the specified Amazon Web Services account ID or group to the list.</p>"""
    remove: NotRequired[
        "capo_ec2.types.create_volume_permission_list.CreateVolumePermissionList"
    ]
    """<p>Removes the specified Amazon Web Services account ID or group from the list.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVolumePermissionModifications,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "add" in value:
        import capo_ec2.types.create_volume_permission_list

        capo_ec2.types.create_volume_permission_list.serialize_ec2_query(
            value["add"], pairs, f"{key_prefix}Add"
        )
    if "remove" in value:
        import capo_ec2.types.create_volume_permission_list

        capo_ec2.types.create_volume_permission_list.serialize_ec2_query(
            value["remove"], pairs, f"{key_prefix}Remove"
        )


def deserialize_ec2_query(el: Element) -> CreateVolumePermissionModifications:
    out: CreateVolumePermissionModifications = {}  # type: ignore[typeddict-item]
    child_add = el.find("Add")
    if child_add is not None:
        import capo_ec2.types.create_volume_permission_list

        out["add"] = capo_ec2.types.create_volume_permission_list.deserialize_ec2_query(
            child_add
        )
    child_remove = el.find("Remove")
    if child_remove is not None:
        import capo_ec2.types.create_volume_permission_list

        out["remove"] = (
            capo_ec2.types.create_volume_permission_list.deserialize_ec2_query(
                child_remove
            )
        )
    return out
