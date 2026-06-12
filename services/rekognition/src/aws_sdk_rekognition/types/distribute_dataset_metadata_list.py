"""Generated from Smithy shape ``com.amazonaws.rekognition#DistributeDatasetMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.distribute_dataset

DistributeDatasetMetadataList: TypeAlias = list[
    "aws_sdk_rekognition.types.distribute_dataset.DistributeDataset"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DistributeDatasetMetadataList) -> list:
    import aws_sdk_rekognition.types.distribute_dataset

    out: list = []
    for item in value:
        out.append(
            aws_sdk_rekognition.types.distribute_dataset.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DistributeDatasetMetadataList:
    import aws_sdk_rekognition.types.distribute_dataset

    out: DistributeDatasetMetadataList = []
    for item in data:
        out.append(
            aws_sdk_rekognition.types.distribute_dataset.deserialize_aws_json_1_1(item)
        )
    return out
