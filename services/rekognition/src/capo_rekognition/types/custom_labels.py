"""Generated from Smithy shape ``com.amazonaws.rekognition#CustomLabels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.custom_label

CustomLabels: TypeAlias = list["capo_rekognition.types.custom_label.CustomLabel"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomLabels) -> list:
    import capo_rekognition.types.custom_label

    out: list = []
    for item in value:
        out.append(capo_rekognition.types.custom_label.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CustomLabels:
    import capo_rekognition.types.custom_label

    out: CustomLabels = []
    for item in data:
        out.append(capo_rekognition.types.custom_label.deserialize_aws_json_1_1(item))
    return out
