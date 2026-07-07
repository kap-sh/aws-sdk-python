"""Generated from Smithy shape ``com.amazonaws.deadline#FieldSortExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.sort_order
    import aws_sdk_deadline.types.string


class FieldSortExpression(TypedDict, closed=True):
    sort_order: "aws_sdk_deadline.types.sort_order.SortOrder"
    """<p>The sort order for the field.</p>"""
    name: "aws_sdk_deadline.types.string.String"
    """<p>The name of the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldSortExpression) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.sort_order

    out["sortOrder"] = aws_sdk_deadline.types.sort_order.serialize_json(
        value["sort_order"]
    )
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> FieldSortExpression:
    out: FieldSortExpression = {}  # type: ignore[typeddict-item]
    if "sortOrder" in data:
        import aws_sdk_deadline.types.sort_order

        out["sort_order"] = aws_sdk_deadline.types.sort_order.deserialize_json(
            data["sortOrder"]
        )
    else:
        raise DeserializationError("FieldSortExpression.sort_order required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("FieldSortExpression.name required")
    return out
