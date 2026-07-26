"""Generated from Smithy shape ``com.amazonaws.deadline#ParameterSortExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.sort_order
    import capo_deadline.types.string


class ParameterSortExpression(TypedDict, closed=True):
    sort_order: "capo_deadline.types.sort_order.SortOrder"
    """<p>The sort order for the parameter.</p>"""
    name: "capo_deadline.types.string.String"
    """<p>The parameter name to sort by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParameterSortExpression) -> dict:
    out: dict = {}
    import capo_deadline.types.sort_order

    out["sortOrder"] = capo_deadline.types.sort_order.serialize_json(
        value["sort_order"]
    )
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> ParameterSortExpression:
    out: ParameterSortExpression = {}  # type: ignore[typeddict-item]
    if "sortOrder" in data:
        import capo_deadline.types.sort_order

        out["sort_order"] = capo_deadline.types.sort_order.deserialize_json(
            data["sortOrder"]
        )
    else:
        raise DeserializationError("ParameterSortExpression.sort_order required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ParameterSortExpression.name required")
    return out
