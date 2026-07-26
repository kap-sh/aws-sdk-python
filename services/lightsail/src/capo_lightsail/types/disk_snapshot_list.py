"""Generated from Smithy shape ``com.amazonaws.lightsail#DiskSnapshotList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.disk_snapshot

DiskSnapshotList: TypeAlias = list["capo_lightsail.types.disk_snapshot.DiskSnapshot"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiskSnapshotList) -> list:
    import capo_lightsail.types.disk_snapshot

    out: list = []
    for item in value:
        out.append(capo_lightsail.types.disk_snapshot.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DiskSnapshotList:
    import capo_lightsail.types.disk_snapshot

    out: DiskSnapshotList = []
    for item in data:
        out.append(capo_lightsail.types.disk_snapshot.deserialize_aws_json_1_1(item))
    return out
