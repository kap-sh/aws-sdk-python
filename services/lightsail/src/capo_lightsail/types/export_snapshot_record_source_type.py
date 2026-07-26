"""Generated from Smithy shape ``com.amazonaws.lightsail#ExportSnapshotRecordSourceType``."""

from typing import Literal, TypeAlias, cast

ExportSnapshotRecordSourceType: TypeAlias = Literal[
    "InstanceSnapshot",
    "DiskSnapshot",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportSnapshotRecordSourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExportSnapshotRecordSourceType:
    return cast(ExportSnapshotRecordSourceType, data)
