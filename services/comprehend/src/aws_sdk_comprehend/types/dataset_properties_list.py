"""Generated from Smithy shape ``com.amazonaws.comprehend#DatasetPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.dataset_properties

DatasetPropertiesList: TypeAlias = list[
    "aws_sdk_comprehend.types.dataset_properties.DatasetProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetPropertiesList) -> list:
    import aws_sdk_comprehend.types.dataset_properties

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehend.types.dataset_properties.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DatasetPropertiesList:
    import aws_sdk_comprehend.types.dataset_properties

    out: DatasetPropertiesList = []
    for item in data:
        out.append(
            aws_sdk_comprehend.types.dataset_properties.deserialize_aws_json_1_1(item)
        )
    return out
