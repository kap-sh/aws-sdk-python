"""Generated from Smithy shape ``com.amazonaws.textract#FeatureTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_textract.types.feature_type

FeatureTypes: TypeAlias = list["aws_sdk_textract.types.feature_type.FeatureType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeatureTypes) -> list:
    import aws_sdk_textract.types.feature_type

    out: list = []
    for item in value:
        out.append(aws_sdk_textract.types.feature_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FeatureTypes:
    import aws_sdk_textract.types.feature_type

    out: FeatureTypes = []
    for item in data:
        out.append(aws_sdk_textract.types.feature_type.deserialize_aws_json_1_1(item))
    return out
