"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchPermissionList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.launch_permission

LaunchPermissionList: TypeAlias = list[
    "capo_ec2.types.launch_permission.LaunchPermission"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchPermissionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.launch_permission

        capo_ec2.types.launch_permission.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> LaunchPermissionList:
    import capo_ec2.types.launch_permission

    out: LaunchPermissionList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.launch_permission.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> LaunchPermissionList:
    import capo_ec2.types.launch_permission

    out: LaunchPermissionList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.launch_permission.deserialize_ec2_query(child))
    return out
