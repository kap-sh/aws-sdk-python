"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferProductIdFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.offer_product_id_filter_value_list


class OfferProductIdFilter(TypedDict, closed=True):
    value_list: NotRequired[
        "capo_marketplace_catalog.types.offer_product_id_filter_value_list.OfferProductIdFilterValueList"
    ]
    """<p>Allows filtering on the <code>ProductId</code> of an offer with list input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OfferProductIdFilter) -> dict:
    out: dict = {}
    if "value_list" in value:
        import capo_marketplace_catalog.types.offer_product_id_filter_value_list

        out["ValueList"] = (
            capo_marketplace_catalog.types.offer_product_id_filter_value_list.serialize_json(
                value["value_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> OfferProductIdFilter:
    out: OfferProductIdFilter = {}  # type: ignore[typeddict-item]
    if "ValueList" in data:
        import capo_marketplace_catalog.types.offer_product_id_filter_value_list

        out["value_list"] = (
            capo_marketplace_catalog.types.offer_product_id_filter_value_list.deserialize_json(
                data["ValueList"]
            )
        )
    return out
