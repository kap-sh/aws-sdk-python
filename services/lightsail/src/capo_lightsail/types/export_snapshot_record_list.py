"""Generated from Smithy shape ``com.amazonaws.lightsail#ExportSnapshotRecordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.export_snapshot_record

ExportSnapshotRecordList: TypeAlias = list[
    "capo_lightsail.types.export_snapshot_record.ExportSnapshotRecord"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportSnapshotRecordList) -> list:
    import capo_lightsail.types.export_snapshot_record

    out: list = []
    for item in value:
        out.append(
            capo_lightsail.types.export_snapshot_record.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExportSnapshotRecordList:
    import capo_lightsail.types.export_snapshot_record

    out: ExportSnapshotRecordList = []
    for item in data:
        out.append(
            capo_lightsail.types.export_snapshot_record.deserialize_aws_json_1_1(item)
        )
    return out
