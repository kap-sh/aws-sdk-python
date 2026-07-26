"""Generated from Smithy shape ``com.amazonaws.textract#LineItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.line_item_fields

LineItemList: TypeAlias = list["capo_textract.types.line_item_fields.LineItemFields"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LineItemList) -> list:
    import capo_textract.types.line_item_fields

    out: list = []
    for item in value:
        out.append(capo_textract.types.line_item_fields.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LineItemList:
    import capo_textract.types.line_item_fields

    out: LineItemList = []
    for item in data:
        out.append(capo_textract.types.line_item_fields.deserialize_aws_json_1_1(item))
    return out
