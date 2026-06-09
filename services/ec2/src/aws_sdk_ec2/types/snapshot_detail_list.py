"""Generated from Smithy shape ``com.amazonaws.ec2#SnapshotDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.snapshot_detail

SnapshotDetailList: TypeAlias = list["aws_sdk_ec2.types.snapshot_detail.SnapshotDetail"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SnapshotDetailList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.snapshot_detail

        aws_sdk_ec2.types.snapshot_detail.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> SnapshotDetailList:
    import aws_sdk_ec2.types.snapshot_detail

    out: SnapshotDetailList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.snapshot_detail.deserialize_ec2_query(child))
    return out
