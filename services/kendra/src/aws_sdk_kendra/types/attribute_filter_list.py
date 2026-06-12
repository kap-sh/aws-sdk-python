"""Generated from Smithy shape ``com.amazonaws.kendra#AttributeFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.attribute_filter

AttributeFilterList: TypeAlias = list[
    "aws_sdk_kendra.types.attribute_filter.AttributeFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttributeFilterList) -> list:
    import aws_sdk_kendra.types.attribute_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_kendra.types.attribute_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AttributeFilterList:
    import aws_sdk_kendra.types.attribute_filter

    out: AttributeFilterList = []
    for item in data:
        out.append(aws_sdk_kendra.types.attribute_filter.deserialize_aws_json_1_1(item))
    return out
