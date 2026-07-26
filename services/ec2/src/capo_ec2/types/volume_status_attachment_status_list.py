"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeStatusAttachmentStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.volume_status_attachment_status

VolumeStatusAttachmentStatusList: TypeAlias = list[
    "capo_ec2.types.volume_status_attachment_status.VolumeStatusAttachmentStatus"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VolumeStatusAttachmentStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.volume_status_attachment_status

        capo_ec2.types.volume_status_attachment_status.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> VolumeStatusAttachmentStatusList:
    import capo_ec2.types.volume_status_attachment_status

    out: VolumeStatusAttachmentStatusList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.volume_status_attachment_status.deserialize_ec2_query(child)
        )
    return out
