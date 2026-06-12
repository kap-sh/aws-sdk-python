"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferFilters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.offer_availability_end_date_filter
    import aws_sdk_marketplace_catalog.types.offer_buyer_accounts_filter
    import aws_sdk_marketplace_catalog.types.offer_entity_id_filter
    import aws_sdk_marketplace_catalog.types.offer_last_modified_date_filter
    import aws_sdk_marketplace_catalog.types.offer_name_filter
    import aws_sdk_marketplace_catalog.types.offer_product_id_filter
    import aws_sdk_marketplace_catalog.types.offer_release_date_filter
    import aws_sdk_marketplace_catalog.types.offer_resale_authorization_id_filter
    import aws_sdk_marketplace_catalog.types.offer_set_id_filter
    import aws_sdk_marketplace_catalog.types.offer_state_filter
    import aws_sdk_marketplace_catalog.types.offer_targeting_filter


class OfferFilters(TypedDict):
    entity_id: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_entity_id_filter.OfferEntityIdFilter"
    ]
    """<p>Allows filtering on <code>EntityId</code> of an offer.</p>"""
    name: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_name_filter.OfferNameFilter"
    ]
    """<p>Allows filtering on the <code>Name</code> of an offer.</p>"""
    product_id: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_product_id_filter.OfferProductIdFilter"
    ]
    """<p>Allows filtering on the <code>ProductId</code> of an offer.</p>"""
    resale_authorization_id: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_resale_authorization_id_filter.OfferResaleAuthorizationIdFilter"
    ]
    """<p>Allows filtering on the <code>ResaleAuthorizationId</code> of an offer.</p> <note> <p>Not all offers have a <code>ResaleAuthorizationId</code>. The response will only include offers for which you have permissions.</p> </note>"""
    release_date: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_release_date_filter.OfferReleaseDateFilter"
    ]
    """<p>Allows filtering on the <code>ReleaseDate</code> of an offer.</p>"""
    availability_end_date: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_availability_end_date_filter.OfferAvailabilityEndDateFilter"
    ]
    """<p>Allows filtering on the <code>AvailabilityEndDate</code> of an offer.</p>"""
    buyer_accounts: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_buyer_accounts_filter.OfferBuyerAccountsFilter"
    ]
    """<p>Allows filtering on the <code>BuyerAccounts</code> of an offer.</p>"""
    state: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_state_filter.OfferStateFilter"
    ]
    """<p>Allows filtering on the <code>State</code> of an offer.</p>"""
    targeting: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_targeting_filter.OfferTargetingFilter"
    ]
    """<p>Allows filtering on the <code>Targeting</code> of an offer.</p>"""
    last_modified_date: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_last_modified_date_filter.OfferLastModifiedDateFilter"
    ]
    """<p>Allows filtering on the <code>LastModifiedDate</code> of an offer.</p>"""
    offer_set_id: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_set_id_filter.OfferSetIdFilter"
    ]
    """<p>Allows filtering on the <code>OfferSetId</code> of an offer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OfferFilters) -> dict:
    out: dict = {}
    if "entity_id" in value:
        import aws_sdk_marketplace_catalog.types.offer_entity_id_filter

        out["EntityId"] = (
            aws_sdk_marketplace_catalog.types.offer_entity_id_filter.serialize_json(
                value["entity_id"]
            )
        )
    if "name" in value:
        import aws_sdk_marketplace_catalog.types.offer_name_filter

        out["Name"] = (
            aws_sdk_marketplace_catalog.types.offer_name_filter.serialize_json(
                value["name"]
            )
        )
    if "product_id" in value:
        import aws_sdk_marketplace_catalog.types.offer_product_id_filter

        out["ProductId"] = (
            aws_sdk_marketplace_catalog.types.offer_product_id_filter.serialize_json(
                value["product_id"]
            )
        )
    if "resale_authorization_id" in value:
        import aws_sdk_marketplace_catalog.types.offer_resale_authorization_id_filter

        out["ResaleAuthorizationId"] = (
            aws_sdk_marketplace_catalog.types.offer_resale_authorization_id_filter.serialize_json(
                value["resale_authorization_id"]
            )
        )
    if "release_date" in value:
        import aws_sdk_marketplace_catalog.types.offer_release_date_filter

        out["ReleaseDate"] = (
            aws_sdk_marketplace_catalog.types.offer_release_date_filter.serialize_json(
                value["release_date"]
            )
        )
    if "availability_end_date" in value:
        import aws_sdk_marketplace_catalog.types.offer_availability_end_date_filter

        out["AvailabilityEndDate"] = (
            aws_sdk_marketplace_catalog.types.offer_availability_end_date_filter.serialize_json(
                value["availability_end_date"]
            )
        )
    if "buyer_accounts" in value:
        import aws_sdk_marketplace_catalog.types.offer_buyer_accounts_filter

        out["BuyerAccounts"] = (
            aws_sdk_marketplace_catalog.types.offer_buyer_accounts_filter.serialize_json(
                value["buyer_accounts"]
            )
        )
    if "state" in value:
        import aws_sdk_marketplace_catalog.types.offer_state_filter

        out["State"] = (
            aws_sdk_marketplace_catalog.types.offer_state_filter.serialize_json(
                value["state"]
            )
        )
    if "targeting" in value:
        import aws_sdk_marketplace_catalog.types.offer_targeting_filter

        out["Targeting"] = (
            aws_sdk_marketplace_catalog.types.offer_targeting_filter.serialize_json(
                value["targeting"]
            )
        )
    if "last_modified_date" in value:
        import aws_sdk_marketplace_catalog.types.offer_last_modified_date_filter

        out["LastModifiedDate"] = (
            aws_sdk_marketplace_catalog.types.offer_last_modified_date_filter.serialize_json(
                value["last_modified_date"]
            )
        )
    if "offer_set_id" in value:
        import aws_sdk_marketplace_catalog.types.offer_set_id_filter

        out["OfferSetId"] = (
            aws_sdk_marketplace_catalog.types.offer_set_id_filter.serialize_json(
                value["offer_set_id"]
            )
        )
    return out


def deserialize_json(data: dict) -> OfferFilters:
    out: OfferFilters = {}  # type: ignore[typeddict-item]
    if "EntityId" in data:
        import aws_sdk_marketplace_catalog.types.offer_entity_id_filter

        out["entity_id"] = (
            aws_sdk_marketplace_catalog.types.offer_entity_id_filter.deserialize_json(
                data["EntityId"]
            )
        )
    if "Name" in data:
        import aws_sdk_marketplace_catalog.types.offer_name_filter

        out["name"] = (
            aws_sdk_marketplace_catalog.types.offer_name_filter.deserialize_json(
                data["Name"]
            )
        )
    if "ProductId" in data:
        import aws_sdk_marketplace_catalog.types.offer_product_id_filter

        out["product_id"] = (
            aws_sdk_marketplace_catalog.types.offer_product_id_filter.deserialize_json(
                data["ProductId"]
            )
        )
    if "ResaleAuthorizationId" in data:
        import aws_sdk_marketplace_catalog.types.offer_resale_authorization_id_filter

        out["resale_authorization_id"] = (
            aws_sdk_marketplace_catalog.types.offer_resale_authorization_id_filter.deserialize_json(
                data["ResaleAuthorizationId"]
            )
        )
    if "ReleaseDate" in data:
        import aws_sdk_marketplace_catalog.types.offer_release_date_filter

        out["release_date"] = (
            aws_sdk_marketplace_catalog.types.offer_release_date_filter.deserialize_json(
                data["ReleaseDate"]
            )
        )
    if "AvailabilityEndDate" in data:
        import aws_sdk_marketplace_catalog.types.offer_availability_end_date_filter

        out["availability_end_date"] = (
            aws_sdk_marketplace_catalog.types.offer_availability_end_date_filter.deserialize_json(
                data["AvailabilityEndDate"]
            )
        )
    if "BuyerAccounts" in data:
        import aws_sdk_marketplace_catalog.types.offer_buyer_accounts_filter

        out["buyer_accounts"] = (
            aws_sdk_marketplace_catalog.types.offer_buyer_accounts_filter.deserialize_json(
                data["BuyerAccounts"]
            )
        )
    if "State" in data:
        import aws_sdk_marketplace_catalog.types.offer_state_filter

        out["state"] = (
            aws_sdk_marketplace_catalog.types.offer_state_filter.deserialize_json(
                data["State"]
            )
        )
    if "Targeting" in data:
        import aws_sdk_marketplace_catalog.types.offer_targeting_filter

        out["targeting"] = (
            aws_sdk_marketplace_catalog.types.offer_targeting_filter.deserialize_json(
                data["Targeting"]
            )
        )
    if "LastModifiedDate" in data:
        import aws_sdk_marketplace_catalog.types.offer_last_modified_date_filter

        out["last_modified_date"] = (
            aws_sdk_marketplace_catalog.types.offer_last_modified_date_filter.deserialize_json(
                data["LastModifiedDate"]
            )
        )
    if "OfferSetId" in data:
        import aws_sdk_marketplace_catalog.types.offer_set_id_filter

        out["offer_set_id"] = (
            aws_sdk_marketplace_catalog.types.offer_set_id_filter.deserialize_json(
                data["OfferSetId"]
            )
        )
    return out
