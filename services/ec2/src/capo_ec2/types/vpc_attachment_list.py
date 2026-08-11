"""Generated from Smithy shape ``com.amazonaws.ec2#VpcAttachmentList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpc_attachment

VpcAttachmentList: TypeAlias = list["capo_ec2.types.vpc_attachment.VpcAttachment"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcAttachmentList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.vpc_attachment

        capo_ec2.types.vpc_attachment.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> VpcAttachmentList:
    import capo_ec2.types.vpc_attachment

    out: VpcAttachmentList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.vpc_attachment.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> VpcAttachmentList:
    import capo_ec2.types.vpc_attachment

    out: VpcAttachmentList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.vpc_attachment.deserialize_ec2_query(child))
    return out
