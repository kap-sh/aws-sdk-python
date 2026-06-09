"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeRecycleBinInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.volume_recycle_bin_info

VolumeRecycleBinInfoList: TypeAlias = list[
    "aws_sdk_ec2.types.volume_recycle_bin_info.VolumeRecycleBinInfo"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VolumeRecycleBinInfoList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.volume_recycle_bin_info

        aws_sdk_ec2.types.volume_recycle_bin_info.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> VolumeRecycleBinInfoList:
    import aws_sdk_ec2.types.volume_recycle_bin_info

    out: VolumeRecycleBinInfoList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.volume_recycle_bin_info.deserialize_ec2_query(child)
        )
    return out
