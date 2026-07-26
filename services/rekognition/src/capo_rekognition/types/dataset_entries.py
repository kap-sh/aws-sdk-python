"""Generated from Smithy shape ``com.amazonaws.rekognition#DatasetEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.dataset_entry

DatasetEntries: TypeAlias = list["capo_rekognition.types.dataset_entry.DatasetEntry"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetEntries) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DatasetEntries:
    return list(data)
