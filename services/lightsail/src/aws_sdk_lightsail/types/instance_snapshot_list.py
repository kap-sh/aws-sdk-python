"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceSnapshotList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.instance_snapshot

InstanceSnapshotList: TypeAlias = list[
    "aws_sdk_lightsail.types.instance_snapshot.InstanceSnapshot"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceSnapshotList) -> list:
    import aws_sdk_lightsail.types.instance_snapshot

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lightsail.types.instance_snapshot.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceSnapshotList:
    import aws_sdk_lightsail.types.instance_snapshot

    out: InstanceSnapshotList = []
    for item in data:
        out.append(
            aws_sdk_lightsail.types.instance_snapshot.deserialize_aws_json_1_1(item)
        )
    return out
