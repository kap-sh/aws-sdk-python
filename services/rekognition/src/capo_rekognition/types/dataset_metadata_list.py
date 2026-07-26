"""Generated from Smithy shape ``com.amazonaws.rekognition#DatasetMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.dataset_metadata

DatasetMetadataList: TypeAlias = list[
    "capo_rekognition.types.dataset_metadata.DatasetMetadata"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetMetadataList) -> list:
    import capo_rekognition.types.dataset_metadata

    out: list = []
    for item in value:
        out.append(capo_rekognition.types.dataset_metadata.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DatasetMetadataList:
    import capo_rekognition.types.dataset_metadata

    out: DatasetMetadataList = []
    for item in data:
        out.append(
            capo_rekognition.types.dataset_metadata.deserialize_aws_json_1_1(item)
        )
    return out
