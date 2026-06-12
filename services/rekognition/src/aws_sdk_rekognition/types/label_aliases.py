"""Generated from Smithy shape ``com.amazonaws.rekognition#LabelAliases``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.label_alias

LabelAliases: TypeAlias = list["aws_sdk_rekognition.types.label_alias.LabelAlias"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelAliases) -> list:
    import aws_sdk_rekognition.types.label_alias

    out: list = []
    for item in value:
        out.append(aws_sdk_rekognition.types.label_alias.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LabelAliases:
    import aws_sdk_rekognition.types.label_alias

    out: LabelAliases = []
    for item in data:
        out.append(aws_sdk_rekognition.types.label_alias.deserialize_aws_json_1_1(item))
    return out
