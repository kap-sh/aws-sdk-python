"""Generated from Smithy shape ``com.amazonaws.glue#Order``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.integer_flag
    import aws_sdk_glue.types.name_string


class Order(TypedDict, closed=True):
    column: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the column.</p>"""
    sort_order: "aws_sdk_glue.types.integer_flag.IntegerFlag"
    """<p>Indicates that the column is sorted in ascending order (<code>== 1</code>), or in descending order (<code>==0</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Order) -> dict:
    out: dict = {}
    out["Column"] = value["column"]
    out["SortOrder"] = value.get("sort_order", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> Order:
    out: Order = {}  # type: ignore[typeddict-item]
    if "Column" in data:
        out["column"] = data["Column"]
    else:
        raise DeserializationError("Order.column required")
    if "SortOrder" in data:
        out["sort_order"] = data["SortOrder"]
    else:
        out["sort_order"] = 0
    return out
