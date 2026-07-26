"""Generated from Smithy shape ``com.amazonaws.ec2#IpPermissionList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ip_permission

IpPermissionList: TypeAlias = list["capo_ec2.types.ip_permission.IpPermission"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpPermissionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ip_permission

        capo_ec2.types.ip_permission.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> IpPermissionList:
    import capo_ec2.types.ip_permission

    out: IpPermissionList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.ip_permission.deserialize_ec2_query(child))
    return out
