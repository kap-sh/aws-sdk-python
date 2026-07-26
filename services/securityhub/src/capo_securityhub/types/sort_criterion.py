"""Generated from Smithy shape ``com.amazonaws.securityhub#SortCriterion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.sort_order


class SortCriterion(TypedDict, closed=True):
    field: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The finding attribute used to sort findings.</p>"""
    sort_order: NotRequired["capo_securityhub.types.sort_order.SortOrder"]
    """<p>The order used to sort findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SortCriterion) -> dict:
    out: dict = {}
    if "field" in value:
        out["Field"] = value["field"]
    if "sort_order" in value:
        import capo_securityhub.types.sort_order

        out["SortOrder"] = capo_securityhub.types.sort_order.serialize_json(
            value["sort_order"]
        )
    return out


def deserialize_json(data: dict) -> SortCriterion:
    out: SortCriterion = {}  # type: ignore[typeddict-item]
    if "Field" in data:
        out["field"] = data["Field"]
    if "SortOrder" in data:
        import capo_securityhub.types.sort_order

        out["sort_order"] = capo_securityhub.types.sort_order.deserialize_json(
            data["SortOrder"]
        )
    return out
