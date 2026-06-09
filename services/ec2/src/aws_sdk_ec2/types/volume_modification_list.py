"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeModificationList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.volume_modification

VolumeModificationList: TypeAlias = list[
    "aws_sdk_ec2.types.volume_modification.VolumeModification"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VolumeModificationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.volume_modification

        aws_sdk_ec2.types.volume_modification.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> VolumeModificationList:
    import aws_sdk_ec2.types.volume_modification

    out: VolumeModificationList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.volume_modification.deserialize_ec2_query(child))
    return out
