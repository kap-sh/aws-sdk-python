"""Generated from Smithy shape ``com.amazonaws.textract#LineItemGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.line_item_group

LineItemGroupList: TypeAlias = list["capo_textract.types.line_item_group.LineItemGroup"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LineItemGroupList) -> list:
    import capo_textract.types.line_item_group

    out: list = []
    for item in value:
        out.append(capo_textract.types.line_item_group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LineItemGroupList:
    import capo_textract.types.line_item_group

    out: LineItemGroupList = []
    for item in data:
        out.append(capo_textract.types.line_item_group.deserialize_aws_json_1_1(item))
    return out
