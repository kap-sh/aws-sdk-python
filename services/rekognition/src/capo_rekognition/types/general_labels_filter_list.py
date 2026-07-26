"""Generated from Smithy shape ``com.amazonaws.rekognition#GeneralLabelsFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.general_labels_filter_value

GeneralLabelsFilterList: TypeAlias = list[
    "capo_rekognition.types.general_labels_filter_value.GeneralLabelsFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GeneralLabelsFilterList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> GeneralLabelsFilterList:
    return list(data)
