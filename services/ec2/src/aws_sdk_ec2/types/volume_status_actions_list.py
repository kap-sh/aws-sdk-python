"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeStatusActionsList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.volume_status_action

VolumeStatusActionsList: TypeAlias = list[
    "aws_sdk_ec2.types.volume_status_action.VolumeStatusAction"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VolumeStatusActionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.volume_status_action

        aws_sdk_ec2.types.volume_status_action.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> VolumeStatusActionsList:
    import aws_sdk_ec2.types.volume_status_action

    out: VolumeStatusActionsList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.volume_status_action.deserialize_ec2_query(child))
    return out
