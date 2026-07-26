"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#IngestionJobStatus``."""

from typing import Literal, TypeAlias, cast

IngestionJobStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCESS",
    "FAILED",
    "IMPORT_IN_PROGRESS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngestionJobStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IngestionJobStatus:
    return cast(IngestionJobStatus, data)
