"""Generated from Smithy shape ``com.amazonaws.lightsail#ExportSnapshotRecordSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

ExportSnapshotRecordSourceType: TypeAlias = Literal[
    "InstanceSnapshot",
    "DiskSnapshot",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InstanceSnapshot",
        "DiskSnapshot",
    )
)


def serialize_aws_json_1_1(value: ExportSnapshotRecordSourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExportSnapshotRecordSourceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ExportSnapshotRecordSourceType value: {data!r}"
        )
    return cast(ExportSnapshotRecordSourceType, data)
