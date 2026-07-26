"""Generated from Smithy shape ``com.amazonaws.kendra#SnapshotsDataRecord``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.string

SnapshotsDataRecord: TypeAlias = list["capo_kendra.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotsDataRecord) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SnapshotsDataRecord:
    return list(data)
