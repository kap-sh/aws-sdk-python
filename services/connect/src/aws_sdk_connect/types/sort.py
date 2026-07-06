"""Generated from Smithy shape ``com.amazonaws.connect#Sort``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.sort_order
    import aws_sdk_connect.types.sortable_field_name


class Sort(TypedDict, closed=True):
    field_name: "aws_sdk_connect.types.sortable_field_name.SortableFieldName"
    """<p>The name of the field on which to sort.</p>"""
    order: "aws_sdk_connect.types.sort_order.SortOrder"
    """<p>An ascending or descending sort.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Sort) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.sortable_field_name

    out["FieldName"] = aws_sdk_connect.types.sortable_field_name.serialize_json(
        value["field_name"]
    )
    import aws_sdk_connect.types.sort_order

    out["Order"] = aws_sdk_connect.types.sort_order.serialize_json(value["order"])
    return out


def deserialize_json(data: dict) -> Sort:
    out: Sort = {}  # type: ignore[typeddict-item]
    if "FieldName" in data:
        import aws_sdk_connect.types.sortable_field_name

        out["field_name"] = aws_sdk_connect.types.sortable_field_name.deserialize_json(
            data["FieldName"]
        )
    else:
        raise DeserializationError("Sort.field_name required")
    if "Order" in data:
        import aws_sdk_connect.types.sort_order

        out["order"] = aws_sdk_connect.types.sort_order.deserialize_json(data["Order"])
    else:
        raise DeserializationError("Sort.order required")
    return out
