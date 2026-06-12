"""Generated from Smithy shape ``com.amazonaws.textract#LineItemGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_textract.types.line_item_list
    import aws_sdk_textract.types.u_integer


class LineItemGroup(TypedDict):
    line_item_group_index: NotRequired["aws_sdk_textract.types.u_integer.UInteger"]
    """<p>The number used to identify a specific table in a document. The first table encountered will have a LineItemGroupIndex of 1, the second 2, etc.</p>"""
    line_items: NotRequired["aws_sdk_textract.types.line_item_list.LineItemList"]
    """<p>The breakdown of information on a particular line of a table. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LineItemGroup) -> dict:
    out: dict = {}
    if "line_item_group_index" in value:
        out["LineItemGroupIndex"] = value["line_item_group_index"]
    if "line_items" in value:
        import aws_sdk_textract.types.line_item_list

        out["LineItems"] = aws_sdk_textract.types.line_item_list.serialize_aws_json_1_1(
            value["line_items"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LineItemGroup:
    out: LineItemGroup = {}  # type: ignore[typeddict-item]
    if "LineItemGroupIndex" in data:
        out["line_item_group_index"] = data["LineItemGroupIndex"]
    if "LineItems" in data:
        import aws_sdk_textract.types.line_item_list

        out["line_items"] = (
            aws_sdk_textract.types.line_item_list.deserialize_aws_json_1_1(
                data["LineItems"]
            )
        )
    return out
