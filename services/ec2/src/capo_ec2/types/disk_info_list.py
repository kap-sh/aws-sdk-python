"""Generated from Smithy shape ``com.amazonaws.ec2#DiskInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.disk_info

DiskInfoList: TypeAlias = list["capo_ec2.types.disk_info.DiskInfo"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DiskInfoList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.disk_info

        capo_ec2.types.disk_info.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> DiskInfoList:
    import capo_ec2.types.disk_info

    out: DiskInfoList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.disk_info.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> DiskInfoList:
    import capo_ec2.types.disk_info

    out: DiskInfoList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.disk_info.deserialize_ec2_query(child))
    return out
