"""Generated from Smithy shape ``com.amazonaws.wafv2#TextTransformations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.text_transformation

TextTransformations: TypeAlias = list[
    "capo_wafv2.types.text_transformation.TextTransformation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TextTransformations) -> list:
    import capo_wafv2.types.text_transformation

    out: list = []
    for item in value:
        out.append(capo_wafv2.types.text_transformation.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TextTransformations:
    import capo_wafv2.types.text_transformation

    out: TextTransformations = []
    for item in data:
        out.append(capo_wafv2.types.text_transformation.deserialize_aws_json_1_1(item))
    return out
