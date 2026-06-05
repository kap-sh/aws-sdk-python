"""Generated from Smithy shape ``com.amazonaws.ec2#ImageList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image

ImageList: TypeAlias = list["aws_sdk_ec2.types.image.Image"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.image

        aws_sdk_ec2.types.image.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> ImageList:
    import aws_sdk_ec2.types.image

    out: ImageList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.image.deserialize_ec2_query(child))
    return out
