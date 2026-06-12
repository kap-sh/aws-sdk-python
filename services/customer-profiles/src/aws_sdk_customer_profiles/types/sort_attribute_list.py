"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SortAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.sort_attribute

SortAttributeList: TypeAlias = list[
    "aws_sdk_customer_profiles.types.sort_attribute.SortAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: SortAttributeList) -> list:
    import aws_sdk_customer_profiles.types.sort_attribute

    out: list = []
    for item in value:
        out.append(aws_sdk_customer_profiles.types.sort_attribute.serialize_json(item))
    return out


def deserialize_json(data: list) -> SortAttributeList:
    import aws_sdk_customer_profiles.types.sort_attribute

    out: SortAttributeList = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.sort_attribute.deserialize_json(item)
        )
    return out
