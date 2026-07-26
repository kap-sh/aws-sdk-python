"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVolumePermissionList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.create_volume_permission

CreateVolumePermissionList: TypeAlias = list[
    "capo_ec2.types.create_volume_permission.CreateVolumePermission"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVolumePermissionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.create_volume_permission

        capo_ec2.types.create_volume_permission.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> CreateVolumePermissionList:
    import capo_ec2.types.create_volume_permission

    out: CreateVolumePermissionList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.create_volume_permission.deserialize_ec2_query(child))
    return out
