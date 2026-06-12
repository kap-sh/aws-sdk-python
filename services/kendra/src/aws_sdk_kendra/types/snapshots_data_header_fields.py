"""Generated from Smithy shape ``com.amazonaws.kendra#SnapshotsDataHeaderFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.string

SnapshotsDataHeaderFields: TypeAlias = list["aws_sdk_kendra.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotsDataHeaderFields) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SnapshotsDataHeaderFields:
    return list(data)
