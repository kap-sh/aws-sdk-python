"""Generated from Smithy shape ``com.amazonaws.rekognition#DatasetLabels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.dataset_label

DatasetLabels: TypeAlias = list["aws_sdk_rekognition.types.dataset_label.DatasetLabel"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetLabels) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DatasetLabels:
    return list(data)
