"""Generated from Smithy shape ``com.amazonaws.billingconductor#LineItemFilterValuesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.line_item_filter_value

LineItemFilterValuesList: TypeAlias = list[
    "aws_sdk_billingconductor.types.line_item_filter_value.LineItemFilterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: LineItemFilterValuesList) -> list:
    import aws_sdk_billingconductor.types.line_item_filter_value

    out: list = []
    for item in value:
        out.append(
            aws_sdk_billingconductor.types.line_item_filter_value.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> LineItemFilterValuesList:
    import aws_sdk_billingconductor.types.line_item_filter_value

    out: LineItemFilterValuesList = []
    for item in data:
        out.append(
            aws_sdk_billingconductor.types.line_item_filter_value.deserialize_json(item)
        )
    return out
