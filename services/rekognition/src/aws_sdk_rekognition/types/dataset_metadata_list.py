"""Generated from Smithy shape ``com.amazonaws.rekognition#DatasetMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.dataset_metadata

DatasetMetadataList: TypeAlias = list[
    "aws_sdk_rekognition.types.dataset_metadata.DatasetMetadata"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetMetadataList) -> list:
    import aws_sdk_rekognition.types.dataset_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_rekognition.types.dataset_metadata.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DatasetMetadataList:
    import aws_sdk_rekognition.types.dataset_metadata

    out: DatasetMetadataList = []
    for item in data:
        out.append(
            aws_sdk_rekognition.types.dataset_metadata.deserialize_aws_json_1_1(item)
        )
    return out
