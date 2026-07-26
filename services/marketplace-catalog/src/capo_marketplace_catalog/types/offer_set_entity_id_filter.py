"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferSetEntityIdFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.offer_set_entity_id_filter_value_list


class OfferSetEntityIdFilter(TypedDict, closed=True):
    value_list: NotRequired[
        "capo_marketplace_catalog.types.offer_set_entity_id_filter_value_list.OfferSetEntityIdFilterValueList"
    ]
    """<p>Allows filtering on entity id of an offer set with list input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OfferSetEntityIdFilter) -> dict:
    out: dict = {}
    if "value_list" in value:
        import capo_marketplace_catalog.types.offer_set_entity_id_filter_value_list

        out["ValueList"] = (
            capo_marketplace_catalog.types.offer_set_entity_id_filter_value_list.serialize_json(
                value["value_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> OfferSetEntityIdFilter:
    out: OfferSetEntityIdFilter = {}  # type: ignore[typeddict-item]
    if "ValueList" in data:
        import capo_marketplace_catalog.types.offer_set_entity_id_filter_value_list

        out["value_list"] = (
            capo_marketplace_catalog.types.offer_set_entity_id_filter_value_list.deserialize_json(
                data["ValueList"]
            )
        )
    return out
