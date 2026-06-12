"""Generated from Smithy shape ``com.amazonaws.deadline#ParameterSortExpression``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.sort_order
    import aws_sdk_deadline.types.string


class ParameterSortExpression(TypedDict):
    sort_order: "aws_sdk_deadline.types.sort_order.SortOrder"
    """<p>The sort order for the parameter.</p>"""
    name: "aws_sdk_deadline.types.string.String"
    """<p>The parameter name to sort by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParameterSortExpression) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.sort_order

    out["sortOrder"] = aws_sdk_deadline.types.sort_order.serialize_json(
        value["sort_order"]
    )
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> ParameterSortExpression:
    out: ParameterSortExpression = {}  # type: ignore[typeddict-item]
    if "sortOrder" in data:
        import aws_sdk_deadline.types.sort_order

        out["sort_order"] = aws_sdk_deadline.types.sort_order.deserialize_json(
            data["sortOrder"]
        )
    else:
        raise DeserializationError("ParameterSortExpression.sort_order required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ParameterSortExpression.name required")
    return out
