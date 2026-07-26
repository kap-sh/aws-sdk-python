"""Generated from Smithy shape ``com.amazonaws.rekognition#DatasetLabelDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.dataset_label_description

DatasetLabelDescriptions: TypeAlias = list[
    "capo_rekognition.types.dataset_label_description.DatasetLabelDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetLabelDescriptions) -> list:
    import capo_rekognition.types.dataset_label_description

    out: list = []
    for item in value:
        out.append(
            capo_rekognition.types.dataset_label_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DatasetLabelDescriptions:
    import capo_rekognition.types.dataset_label_description

    out: DatasetLabelDescriptions = []
    for item in data:
        out.append(
            capo_rekognition.types.dataset_label_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
