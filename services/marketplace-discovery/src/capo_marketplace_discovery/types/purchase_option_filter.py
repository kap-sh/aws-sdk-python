"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PurchaseOptionFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.purchase_option_filter_type
    import capo_marketplace_discovery.types.purchase_option_filter_value_list


class PurchaseOptionFilter(TypedDict, closed=True):
    filter_type: "capo_marketplace_discovery.types.purchase_option_filter_type.PurchaseOptionFilterType"
    """<p>The type of filter to apply, such as <code>PRODUCT_ID</code>, <code>VISIBILITY_SCOPE</code>, or <code>PURCHASE_OPTION_TYPE</code>.</p>"""
    filter_values: "capo_marketplace_discovery.types.purchase_option_filter_value_list.PurchaseOptionFilterValueList"
    """<p>The values to filter by. Multiple values within the same filter are combined with OR logic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PurchaseOptionFilter) -> dict:
    out: dict = {}
    import capo_marketplace_discovery.types.purchase_option_filter_type

    out["filterType"] = (
        capo_marketplace_discovery.types.purchase_option_filter_type.serialize_json(
            value["filter_type"]
        )
    )
    import capo_marketplace_discovery.types.purchase_option_filter_value_list

    out["filterValues"] = (
        capo_marketplace_discovery.types.purchase_option_filter_value_list.serialize_json(
            value["filter_values"]
        )
    )
    return out


def deserialize_json(data: dict) -> PurchaseOptionFilter:
    out: PurchaseOptionFilter = {}  # type: ignore[typeddict-item]
    if "filterType" in data:
        import capo_marketplace_discovery.types.purchase_option_filter_type

        out["filter_type"] = (
            capo_marketplace_discovery.types.purchase_option_filter_type.deserialize_json(
                data["filterType"]
            )
        )
    else:
        raise DeserializationError("PurchaseOptionFilter.filter_type required")
    if "filterValues" in data:
        import capo_marketplace_discovery.types.purchase_option_filter_value_list

        out["filter_values"] = (
            capo_marketplace_discovery.types.purchase_option_filter_value_list.deserialize_json(
                data["filterValues"]
            )
        )
    else:
        raise DeserializationError("PurchaseOptionFilter.filter_values required")
    return out
