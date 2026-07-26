"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferBuyerAccountsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.offer_buyer_accounts_filter_wildcard


class OfferBuyerAccountsFilter(TypedDict, closed=True):
    wild_card_value: NotRequired[
        "capo_marketplace_catalog.types.offer_buyer_accounts_filter_wildcard.OfferBuyerAccountsFilterWildcard"
    ]
    """<p>Allows filtering on the <code>BuyerAccounts</code> of an offer with wild card input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OfferBuyerAccountsFilter) -> dict:
    out: dict = {}
    if "wild_card_value" in value:
        out["WildCardValue"] = value["wild_card_value"]
    return out


def deserialize_json(data: dict) -> OfferBuyerAccountsFilter:
    out: OfferBuyerAccountsFilter = {}  # type: ignore[typeddict-item]
    if "WildCardValue" in data:
        out["wild_card_value"] = data["WildCardValue"]
    return out
