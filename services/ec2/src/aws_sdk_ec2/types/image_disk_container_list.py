"""Generated from Smithy shape ``com.amazonaws.ec2#ImageDiskContainerList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_disk_container

ImageDiskContainerList: TypeAlias = list[
    "aws_sdk_ec2.types.image_disk_container.ImageDiskContainer"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageDiskContainerList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.image_disk_container

        aws_sdk_ec2.types.image_disk_container.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> ImageDiskContainerList:
    import aws_sdk_ec2.types.image_disk_container

    out: ImageDiskContainerList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.image_disk_container.deserialize_ec2_query(child))
    return out
