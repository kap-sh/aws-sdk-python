"""Generated from Smithy shape ``com.amazonaws.lightsail#AutoSnapshotDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.auto_snapshot_details

AutoSnapshotDetailsList: TypeAlias = list[
    "capo_lightsail.types.auto_snapshot_details.AutoSnapshotDetails"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoSnapshotDetailsList) -> list:
    import capo_lightsail.types.auto_snapshot_details

    out: list = []
    for item in value:
        out.append(
            capo_lightsail.types.auto_snapshot_details.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AutoSnapshotDetailsList:
    import capo_lightsail.types.auto_snapshot_details

    out: AutoSnapshotDetailsList = []
    for item in data:
        out.append(
            capo_lightsail.types.auto_snapshot_details.deserialize_aws_json_1_1(item)
        )
    return out
