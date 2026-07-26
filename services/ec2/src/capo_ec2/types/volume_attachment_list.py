"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeAttachmentList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.volume_attachment

VolumeAttachmentList: TypeAlias = list[
    "capo_ec2.types.volume_attachment.VolumeAttachment"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VolumeAttachmentList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.volume_attachment

        capo_ec2.types.volume_attachment.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> VolumeAttachmentList:
    import capo_ec2.types.volume_attachment

    out: VolumeAttachmentList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.volume_attachment.deserialize_ec2_query(child))
    return out
