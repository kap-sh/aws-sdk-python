"""Generated from Smithy shape ``com.amazonaws.customerprofiles#LayoutList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.layout_item

LayoutList: TypeAlias = list["aws_sdk_customer_profiles.types.layout_item.LayoutItem"]


# --- restJson1 ser/de ---
def serialize_json(value: LayoutList) -> list:
    import aws_sdk_customer_profiles.types.layout_item

    out: list = []
    for item in value:
        out.append(aws_sdk_customer_profiles.types.layout_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> LayoutList:
    import aws_sdk_customer_profiles.types.layout_item

    out: LayoutList = []
    for item in data:
        out.append(aws_sdk_customer_profiles.types.layout_item.deserialize_json(item))
    return out
