"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#Sort``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.sort_by
    import capo_marketplace_agreement.types.sort_order


class Sort(TypedDict, closed=True):
    sort_by: NotRequired["capo_marketplace_agreement.types.sort_by.SortBy"]
    """<p>The attribute on which the data is grouped, which can be by <code>StartTime</code> and <code>EndTime</code>. The default value is <code>EndTime</code>.</p>"""
    sort_order: NotRequired["capo_marketplace_agreement.types.sort_order.SortOrder"]
    """<p>The sorting order, which can be <code>ASCENDING</code> or <code>DESCENDING</code>. The default value is <code>DESCENDING</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Sort) -> dict:
    out: dict = {}
    if "sort_by" in value:
        out["sortBy"] = value["sort_by"]
    if "sort_order" in value:
        import capo_marketplace_agreement.types.sort_order

        out["sortOrder"] = (
            capo_marketplace_agreement.types.sort_order.serialize_aws_json_1_0(
                value["sort_order"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Sort:
    out: Sort = {}  # type: ignore[typeddict-item]
    if "sortBy" in data:
        out["sort_by"] = data["sortBy"]
    if "sortOrder" in data:
        import capo_marketplace_agreement.types.sort_order

        out["sort_order"] = (
            capo_marketplace_agreement.types.sort_order.deserialize_aws_json_1_0(
                data["sortOrder"]
            )
        )
    return out
