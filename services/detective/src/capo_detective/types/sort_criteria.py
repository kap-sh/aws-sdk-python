"""Generated from Smithy shape ``com.amazonaws.detective#SortCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_detective.types.field
    import capo_detective.types.sort_order


class SortCriteria(TypedDict, closed=True):
    field: NotRequired["capo_detective.types.field.Field"]
    """<p>Represents the <code>Field</code> attribute to sort investigations.</p>"""
    sort_order: NotRequired["capo_detective.types.sort_order.SortOrder"]
    """<p>The order by which the sorted findings are displayed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SortCriteria) -> dict:
    out: dict = {}
    if "field" in value:
        import capo_detective.types.field

        out["Field"] = capo_detective.types.field.serialize_json(value["field"])
    if "sort_order" in value:
        import capo_detective.types.sort_order

        out["SortOrder"] = capo_detective.types.sort_order.serialize_json(
            value["sort_order"]
        )
    return out


def deserialize_json(data: dict) -> SortCriteria:
    out: SortCriteria = {}  # type: ignore[typeddict-item]
    if "Field" in data:
        import capo_detective.types.field

        out["field"] = capo_detective.types.field.deserialize_json(data["Field"])
    if "SortOrder" in data:
        import capo_detective.types.sort_order

        out["sort_order"] = capo_detective.types.sort_order.deserialize_json(
            data["SortOrder"]
        )
    return out
