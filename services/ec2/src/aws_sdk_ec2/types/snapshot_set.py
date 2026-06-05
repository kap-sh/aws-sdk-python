"""Generated from Smithy shape ``com.amazonaws.ec2#SnapshotSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.snapshot_info

SnapshotSet: TypeAlias = list["aws_sdk_ec2.types.snapshot_info.SnapshotInfo"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SnapshotSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.snapshot_info

        aws_sdk_ec2.types.snapshot_info.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> SnapshotSet:
    import aws_sdk_ec2.types.snapshot_info

    out: SnapshotSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.snapshot_info.deserialize_ec2_query(child))
    return out
