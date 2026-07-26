"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DatasetStatus``."""

from typing import Literal, TypeAlias, cast

DatasetStatus: TypeAlias = Literal[
    "CREATED",
    "INGESTION_IN_PROGRESS",
    "ACTIVE",
    "IMPORT_IN_PROGRESS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DatasetStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DatasetStatus:
    return cast(DatasetStatus, data)
