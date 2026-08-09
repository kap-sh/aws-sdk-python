"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeRecycleBinInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.volume_recycle_bin_info

VolumeRecycleBinInfoList: TypeAlias = list[
    "capo_ec2.types.volume_recycle_bin_info.VolumeRecycleBinInfo"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VolumeRecycleBinInfoList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.volume_recycle_bin_info

        capo_ec2.types.volume_recycle_bin_info.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> VolumeRecycleBinInfoList:
    import capo_ec2.types.volume_recycle_bin_info

    out: VolumeRecycleBinInfoList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.volume_recycle_bin_info.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> VolumeRecycleBinInfoList:
    import capo_ec2.types.volume_recycle_bin_info

    out: VolumeRecycleBinInfoList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.volume_recycle_bin_info.deserialize_ec2_query(child))
    return out
