"""Generated from Smithy shape ``com.amazonaws.odb#DbServerPatchingStatus``."""

from typing import Literal, TypeAlias, cast

DbServerPatchingStatus: TypeAlias = Literal[
    "COMPLETE",
    "FAILED",
    "MAINTENANCE_IN_PROGRESS",
    "SCHEDULED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbServerPatchingStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DbServerPatchingStatus:
    return cast(DbServerPatchingStatus, data)
