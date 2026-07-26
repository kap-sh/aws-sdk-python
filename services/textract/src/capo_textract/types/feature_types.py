"""Generated from Smithy shape ``com.amazonaws.textract#FeatureTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.feature_type

FeatureTypes: TypeAlias = list["capo_textract.types.feature_type.FeatureType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeatureTypes) -> list:
    import capo_textract.types.feature_type

    out: list = []
    for item in value:
        out.append(capo_textract.types.feature_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FeatureTypes:
    import capo_textract.types.feature_type

    out: FeatureTypes = []
    for item in data:
        out.append(capo_textract.types.feature_type.deserialize_aws_json_1_1(item))
    return out
