"""Generated from Smithy shape ``com.amazonaws.connect#PredefinedAttributePurposeNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.predefined_attribute_purpose_name

PredefinedAttributePurposeNameList: TypeAlias = list[
    "aws_sdk_connect.types.predefined_attribute_purpose_name.PredefinedAttributePurposeName"
]


# --- restJson1 ser/de ---
def serialize_json(value: PredefinedAttributePurposeNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> PredefinedAttributePurposeNameList:
    return list(data)
