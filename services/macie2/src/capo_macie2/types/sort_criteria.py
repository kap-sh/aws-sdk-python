"""Generated from Smithy shape ``com.amazonaws.macie2#SortCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__string
    import capo_macie2.types.order_by


class SortCriteria(TypedDict, closed=True):
    attribute_name: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The name of the property to sort the results by. Valid values are: count, createdAt, policyDetails.action.apiCallDetails.firstSeen, policyDetails.action.apiCallDetails.lastSeen, resourcesAffected, severity.score, type, and updatedAt.</p>"""
    order_by: NotRequired["capo_macie2.types.order_by.OrderBy"]
    """<p>The sort order to apply to the results, based on the value for the property specified by the attributeName property. Valid values are: ASC, sort the results in ascending order; and, DESC, sort the results in descending order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SortCriteria) -> dict:
    out: dict = {}
    if "attribute_name" in value:
        out["attributeName"] = value["attribute_name"]
    if "order_by" in value:
        import capo_macie2.types.order_by

        out["orderBy"] = capo_macie2.types.order_by.serialize_json(value["order_by"])
    return out


def deserialize_json(data: dict) -> SortCriteria:
    out: SortCriteria = {}  # type: ignore[typeddict-item]
    if "attributeName" in data:
        out["attribute_name"] = data["attributeName"]
    if "orderBy" in data:
        import capo_macie2.types.order_by

        out["order_by"] = capo_macie2.types.order_by.deserialize_json(data["orderBy"])
    return out
