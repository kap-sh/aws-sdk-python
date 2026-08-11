"""Generated from Smithy shape ``com.amazonaws.ec2#FpgaImageList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.fpga_image

FpgaImageList: TypeAlias = list["capo_ec2.types.fpga_image.FpgaImage"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FpgaImageList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.fpga_image

        capo_ec2.types.fpga_image.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> FpgaImageList:
    import capo_ec2.types.fpga_image

    out: FpgaImageList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.fpga_image.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> FpgaImageList:
    import capo_ec2.types.fpga_image

    out: FpgaImageList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.fpga_image.deserialize_ec2_query(child))
    return out
