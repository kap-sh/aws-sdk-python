"""Generated from Smithy shape ``com.amazonaws.ec2#LockedSnapshotsInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.locked_snapshots_info

LockedSnapshotsInfoList: TypeAlias = list[
    "aws_sdk_ec2.types.locked_snapshots_info.LockedSnapshotsInfo"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LockedSnapshotsInfoList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.locked_snapshots_info

        aws_sdk_ec2.types.locked_snapshots_info.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> LockedSnapshotsInfoList:
    import aws_sdk_ec2.types.locked_snapshots_info

    out: LockedSnapshotsInfoList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.locked_snapshots_info.deserialize_ec2_query(child))
    return out
