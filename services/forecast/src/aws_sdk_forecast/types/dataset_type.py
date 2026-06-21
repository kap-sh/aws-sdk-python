"""Generated from Smithy shape ``com.amazonaws.forecast#DatasetType``."""

from typing import Literal, TypeAlias, cast

DatasetType: TypeAlias = Literal[
    "TARGET_TIME_SERIES",
    "RELATED_TIME_SERIES",
    "ITEM_METADATA",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DatasetType:
    return cast(DatasetType, data)
