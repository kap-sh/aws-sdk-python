"""Generated from Smithy shape ``com.amazonaws.ec2#StaleIpPermissionSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.stale_ip_permission

StaleIpPermissionSet: TypeAlias = list[
    "capo_ec2.types.stale_ip_permission.StaleIpPermission"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: StaleIpPermissionSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.stale_ip_permission

        capo_ec2.types.stale_ip_permission.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> StaleIpPermissionSet:
    import capo_ec2.types.stale_ip_permission

    out: StaleIpPermissionSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.stale_ip_permission.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> StaleIpPermissionSet:
    import capo_ec2.types.stale_ip_permission

    out: StaleIpPermissionSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.stale_ip_permission.deserialize_ec2_query(child))
    return out
