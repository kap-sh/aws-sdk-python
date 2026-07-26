"""Generated from Smithy shape ``com.amazonaws.rekognition#LabelCategories``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.label_category

LabelCategories: TypeAlias = list["capo_rekognition.types.label_category.LabelCategory"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelCategories) -> list:
    import capo_rekognition.types.label_category

    out: list = []
    for item in value:
        out.append(capo_rekognition.types.label_category.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LabelCategories:
    import capo_rekognition.types.label_category

    out: LabelCategories = []
    for item in data:
        out.append(capo_rekognition.types.label_category.deserialize_aws_json_1_1(item))
    return out
