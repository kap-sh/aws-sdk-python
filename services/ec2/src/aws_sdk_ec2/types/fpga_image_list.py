"""Generated from Smithy shape ``com.amazonaws.ec2#FpgaImageList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fpga_image

FpgaImageList: TypeAlias = list["aws_sdk_ec2.types.fpga_image.FpgaImage"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FpgaImageList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.fpga_image

        aws_sdk_ec2.types.fpga_image.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> FpgaImageList:
    import aws_sdk_ec2.types.fpga_image

    out: FpgaImageList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.fpga_image.deserialize_ec2_query(child))
    return out
