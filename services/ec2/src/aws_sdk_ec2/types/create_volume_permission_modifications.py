"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVolumePermissionModifications``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_volume_permission_list


class CreateVolumePermissionModifications(TypedDict, closed=True):
    add: NotRequired[
        "aws_sdk_ec2.types.create_volume_permission_list.CreateVolumePermissionList"
    ]
    """<p>Adds the specified Amazon Web Services account ID or group to the list.</p>"""
    remove: NotRequired[
        "aws_sdk_ec2.types.create_volume_permission_list.CreateVolumePermissionList"
    ]
    """<p>Removes the specified Amazon Web Services account ID or group from the list.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVolumePermissionModifications,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "add" in value:
        import aws_sdk_ec2.types.create_volume_permission_list

        aws_sdk_ec2.types.create_volume_permission_list.serialize_ec2_query(
            value["add"], pairs, f"{prefix}.Add"
        )
    if "remove" in value:
        import aws_sdk_ec2.types.create_volume_permission_list

        aws_sdk_ec2.types.create_volume_permission_list.serialize_ec2_query(
            value["remove"], pairs, f"{prefix}.Remove"
        )


def deserialize_ec2_query(el: Element) -> CreateVolumePermissionModifications:
    out: CreateVolumePermissionModifications = {}  # type: ignore[typeddict-item]
    if el.find("Add") is not None:
        import aws_sdk_ec2.types.create_volume_permission_list

        out["add"] = (
            aws_sdk_ec2.types.create_volume_permission_list.deserialize_ec2_query(
                el, "Add"
            )
        )
    if el.find("Remove") is not None:
        import aws_sdk_ec2.types.create_volume_permission_list

        out["remove"] = (
            aws_sdk_ec2.types.create_volume_permission_list.deserialize_ec2_query(
                el, "Remove"
            )
        )
    return out
