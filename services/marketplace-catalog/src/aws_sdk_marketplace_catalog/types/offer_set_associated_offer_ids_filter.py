"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferSetAssociatedOfferIdsFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.offer_set_associated_offer_ids_filter_value_list


class OfferSetAssociatedOfferIdsFilter(TypedDict):
    value_list: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_set_associated_offer_ids_filter_value_list.OfferSetAssociatedOfferIdsFilterValueList"
    ]
    """<p>Allows filtering on the <code>AssociatedOfferIds</code> of an offer set with list input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OfferSetAssociatedOfferIdsFilter) -> dict:
    out: dict = {}
    if "value_list" in value:
        import aws_sdk_marketplace_catalog.types.offer_set_associated_offer_ids_filter_value_list

        out["ValueList"] = (
            aws_sdk_marketplace_catalog.types.offer_set_associated_offer_ids_filter_value_list.serialize_json(
                value["value_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> OfferSetAssociatedOfferIdsFilter:
    out: OfferSetAssociatedOfferIdsFilter = {}  # type: ignore[typeddict-item]
    if "ValueList" in data:
        import aws_sdk_marketplace_catalog.types.offer_set_associated_offer_ids_filter_value_list

        out["value_list"] = (
            aws_sdk_marketplace_catalog.types.offer_set_associated_offer_ids_filter_value_list.deserialize_json(
                data["ValueList"]
            )
        )
    return out
