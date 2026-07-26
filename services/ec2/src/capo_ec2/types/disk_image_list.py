"""Generated from Smithy shape ``com.amazonaws.ec2#DiskImageList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.disk_image

DiskImageList: TypeAlias = list["capo_ec2.types.disk_image.DiskImage"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DiskImageList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.disk_image

        capo_ec2.types.disk_image.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> DiskImageList:
    import capo_ec2.types.disk_image

    out: DiskImageList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.disk_image.deserialize_ec2_query(child))
    return out
