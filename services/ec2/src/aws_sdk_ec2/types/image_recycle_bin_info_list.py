"""Generated from Smithy shape ``com.amazonaws.ec2#ImageRecycleBinInfoList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_recycle_bin_info

ImageRecycleBinInfoList: TypeAlias = list[
    "aws_sdk_ec2.types.image_recycle_bin_info.ImageRecycleBinInfo"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageRecycleBinInfoList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.image_recycle_bin_info

        aws_sdk_ec2.types.image_recycle_bin_info.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> ImageRecycleBinInfoList:
    import aws_sdk_ec2.types.image_recycle_bin_info

    out: ImageRecycleBinInfoList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.image_recycle_bin_info.deserialize_ec2_query(child)
        )
    return out
