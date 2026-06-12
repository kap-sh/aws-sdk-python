"""Generated from Smithy shape ``com.amazonaws.connect#PredefinedAttributeSearchSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.predefined_attribute

PredefinedAttributeSearchSummaryList: TypeAlias = list[
    "aws_sdk_connect.types.predefined_attribute.PredefinedAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: PredefinedAttributeSearchSummaryList) -> list:
    import aws_sdk_connect.types.predefined_attribute

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.predefined_attribute.serialize_json(item))
    return out


def deserialize_json(data: list) -> PredefinedAttributeSearchSummaryList:
    import aws_sdk_connect.types.predefined_attribute

    out: PredefinedAttributeSearchSummaryList = []
    for item in data:
        out.append(aws_sdk_connect.types.predefined_attribute.deserialize_json(item))
    return out
