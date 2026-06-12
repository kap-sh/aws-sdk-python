"""Generated from Smithy shape ``com.amazonaws.wafv2#TextTransformations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.text_transformation

TextTransformations: TypeAlias = list[
    "aws_sdk_wafv2.types.text_transformation.TextTransformation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TextTransformations) -> list:
    import aws_sdk_wafv2.types.text_transformation

    out: list = []
    for item in value:
        out.append(aws_sdk_wafv2.types.text_transformation.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TextTransformations:
    import aws_sdk_wafv2.types.text_transformation

    out: TextTransformations = []
    for item in data:
        out.append(
            aws_sdk_wafv2.types.text_transformation.deserialize_aws_json_1_1(item)
        )
    return out
