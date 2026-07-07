"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.date_time_iso8601
    import aws_sdk_marketplace_catalog.types.offer_buyer_accounts_list
    import aws_sdk_marketplace_catalog.types.offer_name_string
    import aws_sdk_marketplace_catalog.types.offer_product_id_string
    import aws_sdk_marketplace_catalog.types.offer_resale_authorization_id_string
    import aws_sdk_marketplace_catalog.types.offer_set_id_string
    import aws_sdk_marketplace_catalog.types.offer_state_string
    import aws_sdk_marketplace_catalog.types.offer_targeting_list


class OfferSummary(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_name_string.OfferNameString"
    ]
    """<p>The name of the offer.</p>"""
    product_id: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_product_id_string.OfferProductIdString"
    ]
    """<p>The product ID of the offer.</p>"""
    resale_authorization_id: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_resale_authorization_id_string.OfferResaleAuthorizationIdString"
    ]
    """<p>The ResaleAuthorizationId of the offer.</p>"""
    release_date: NotRequired[
        "aws_sdk_marketplace_catalog.types.date_time_iso8601.DateTimeISO8601"
    ]
    """<p>The release date of the offer.</p>"""
    availability_end_date: NotRequired[
        "aws_sdk_marketplace_catalog.types.date_time_iso8601.DateTimeISO8601"
    ]
    """<p>The availability end date of the offer.</p>"""
    buyer_accounts: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_buyer_accounts_list.OfferBuyerAccountsList"
    ]
    """<p>The buyer accounts in the offer.</p>"""
    state: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_state_string.OfferStateString"
    ]
    """<p>The status of the offer.</p>"""
    targeting: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_targeting_list.OfferTargetingList"
    ]
    """<p>The targeting in the offer.</p>"""
    offer_set_id: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_set_id_string.OfferSetIdString"
    ]
    """<p>The offer set ID of the offer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OfferSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
    if "resale_authorization_id" in value:
        out["ResaleAuthorizationId"] = value["resale_authorization_id"]
    if "release_date" in value:
        out["ReleaseDate"] = value["release_date"]
    if "availability_end_date" in value:
        out["AvailabilityEndDate"] = value["availability_end_date"]
    if "buyer_accounts" in value:
        import aws_sdk_marketplace_catalog.types.offer_buyer_accounts_list

        out["BuyerAccounts"] = (
            aws_sdk_marketplace_catalog.types.offer_buyer_accounts_list.serialize_json(
                value["buyer_accounts"]
            )
        )
    if "state" in value:
        import aws_sdk_marketplace_catalog.types.offer_state_string

        out["State"] = (
            aws_sdk_marketplace_catalog.types.offer_state_string.serialize_json(
                value["state"]
            )
        )
    if "targeting" in value:
        import aws_sdk_marketplace_catalog.types.offer_targeting_list

        out["Targeting"] = (
            aws_sdk_marketplace_catalog.types.offer_targeting_list.serialize_json(
                value["targeting"]
            )
        )
    if "offer_set_id" in value:
        out["OfferSetId"] = value["offer_set_id"]
    return out


def deserialize_json(data: dict) -> OfferSummary:
    out: OfferSummary = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ProductId" in data:
        out["product_id"] = data["ProductId"]
    if "ResaleAuthorizationId" in data:
        out["resale_authorization_id"] = data["ResaleAuthorizationId"]
    if "ReleaseDate" in data:
        out["release_date"] = data["ReleaseDate"]
    if "AvailabilityEndDate" in data:
        out["availability_end_date"] = data["AvailabilityEndDate"]
    if "BuyerAccounts" in data:
        import aws_sdk_marketplace_catalog.types.offer_buyer_accounts_list

        out["buyer_accounts"] = (
            aws_sdk_marketplace_catalog.types.offer_buyer_accounts_list.deserialize_json(
                data["BuyerAccounts"]
            )
        )
    if "State" in data:
        import aws_sdk_marketplace_catalog.types.offer_state_string

        out["state"] = (
            aws_sdk_marketplace_catalog.types.offer_state_string.deserialize_json(
                data["State"]
            )
        )
    if "Targeting" in data:
        import aws_sdk_marketplace_catalog.types.offer_targeting_list

        out["targeting"] = (
            aws_sdk_marketplace_catalog.types.offer_targeting_list.deserialize_json(
                data["Targeting"]
            )
        )
    if "OfferSetId" in data:
        out["offer_set_id"] = data["OfferSetId"]
    return out
