"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResaleAuthorizationFilters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.resale_authorization_availability_end_date_filter
    import aws_sdk_marketplace_catalog.types.resale_authorization_created_date_filter
    import aws_sdk_marketplace_catalog.types.resale_authorization_entity_id_filter
    import aws_sdk_marketplace_catalog.types.resale_authorization_last_modified_date_filter
    import aws_sdk_marketplace_catalog.types.resale_authorization_manufacturer_account_id_filter
    import aws_sdk_marketplace_catalog.types.resale_authorization_manufacturer_legal_name_filter
    import aws_sdk_marketplace_catalog.types.resale_authorization_name_filter
    import aws_sdk_marketplace_catalog.types.resale_authorization_offer_extended_status_filter
    import aws_sdk_marketplace_catalog.types.resale_authorization_product_id_filter
    import aws_sdk_marketplace_catalog.types.resale_authorization_product_name_filter
    import aws_sdk_marketplace_catalog.types.resale_authorization_reseller_account_id_filter
    import aws_sdk_marketplace_catalog.types.resale_authorization_reseller_legal_name_filter
    import aws_sdk_marketplace_catalog.types.resale_authorization_status_filter


class ResaleAuthorizationFilters(TypedDict):
    entity_id: NotRequired[
        "aws_sdk_marketplace_catalog.types.resale_authorization_entity_id_filter.ResaleAuthorizationEntityIdFilter"
    ]
    """<p>Allows filtering on the <code>EntityId</code> of a ResaleAuthorization.</p>"""
    name: NotRequired[
        "aws_sdk_marketplace_catalog.types.resale_authorization_name_filter.ResaleAuthorizationNameFilter"
    ]
    """<p>Allows filtering on the <code>Name</code> of a ResaleAuthorization.</p>"""
    product_id: NotRequired[
        "aws_sdk_marketplace_catalog.types.resale_authorization_product_id_filter.ResaleAuthorizationProductIdFilter"
    ]
    """<p>Allows filtering on the <code>ProductId</code> of a ResaleAuthorization.</p>"""
    created_date: NotRequired[
        "aws_sdk_marketplace_catalog.types.resale_authorization_created_date_filter.ResaleAuthorizationCreatedDateFilter"
    ]
    """<p>Allows filtering on the <code>CreatedDate</code> of a ResaleAuthorization.</p>"""
    availability_end_date: NotRequired[
        "aws_sdk_marketplace_catalog.types.resale_authorization_availability_end_date_filter.ResaleAuthorizationAvailabilityEndDateFilter"
    ]
    """<p>Allows filtering on the <code>AvailabilityEndDate</code> of a ResaleAuthorization.</p>"""
    manufacturer_account_id: NotRequired[
        "aws_sdk_marketplace_catalog.types.resale_authorization_manufacturer_account_id_filter.ResaleAuthorizationManufacturerAccountIdFilter"
    ]
    """<p>Allows filtering on the <code>ManufacturerAccountId</code> of a ResaleAuthorization.</p>"""
    product_name: NotRequired[
        "aws_sdk_marketplace_catalog.types.resale_authorization_product_name_filter.ResaleAuthorizationProductNameFilter"
    ]
    """<p>Allows filtering on the <code>ProductName</code> of a ResaleAuthorization.</p>"""
    manufacturer_legal_name: NotRequired[
        "aws_sdk_marketplace_catalog.types.resale_authorization_manufacturer_legal_name_filter.ResaleAuthorizationManufacturerLegalNameFilter"
    ]
    """<p>Allows filtering on the <code>ManufacturerLegalName</code> of a ResaleAuthorization.</p>"""
    reseller_account_id: NotRequired[
        "aws_sdk_marketplace_catalog.types.resale_authorization_reseller_account_id_filter.ResaleAuthorizationResellerAccountIDFilter"
    ]
    """<p>Allows filtering on the <code>ResellerAccountID</code> of a ResaleAuthorization.</p>"""
    reseller_legal_name: NotRequired[
        "aws_sdk_marketplace_catalog.types.resale_authorization_reseller_legal_name_filter.ResaleAuthorizationResellerLegalNameFilter"
    ]
    """<p>Allows filtering on the <code>ResellerLegalName</code> of a ResaleAuthorization.</p>"""
    status: NotRequired[
        "aws_sdk_marketplace_catalog.types.resale_authorization_status_filter.ResaleAuthorizationStatusFilter"
    ]
    """<p>Allows filtering on the <code>Status</code> of a ResaleAuthorization.</p>"""
    offer_extended_status: NotRequired[
        "aws_sdk_marketplace_catalog.types.resale_authorization_offer_extended_status_filter.ResaleAuthorizationOfferExtendedStatusFilter"
    ]
    """<p>Allows filtering on the <code>OfferExtendedStatus</code> of a ResaleAuthorization.</p>"""
    last_modified_date: NotRequired[
        "aws_sdk_marketplace_catalog.types.resale_authorization_last_modified_date_filter.ResaleAuthorizationLastModifiedDateFilter"
    ]
    """<p>Allows filtering on the <code>LastModifiedDate</code> of a ResaleAuthorization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResaleAuthorizationFilters) -> dict:
    out: dict = {}
    if "entity_id" in value:
        import aws_sdk_marketplace_catalog.types.resale_authorization_entity_id_filter

        out["EntityId"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_entity_id_filter.serialize_json(
                value["entity_id"]
            )
        )
    if "name" in value:
        import aws_sdk_marketplace_catalog.types.resale_authorization_name_filter

        out["Name"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_name_filter.serialize_json(
                value["name"]
            )
        )
    if "product_id" in value:
        import aws_sdk_marketplace_catalog.types.resale_authorization_product_id_filter

        out["ProductId"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_product_id_filter.serialize_json(
                value["product_id"]
            )
        )
    if "created_date" in value:
        import aws_sdk_marketplace_catalog.types.resale_authorization_created_date_filter

        out["CreatedDate"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_created_date_filter.serialize_json(
                value["created_date"]
            )
        )
    if "availability_end_date" in value:
        import aws_sdk_marketplace_catalog.types.resale_authorization_availability_end_date_filter

        out["AvailabilityEndDate"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_availability_end_date_filter.serialize_json(
                value["availability_end_date"]
            )
        )
    if "manufacturer_account_id" in value:
        import aws_sdk_marketplace_catalog.types.resale_authorization_manufacturer_account_id_filter

        out["ManufacturerAccountId"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_manufacturer_account_id_filter.serialize_json(
                value["manufacturer_account_id"]
            )
        )
    if "product_name" in value:
        import aws_sdk_marketplace_catalog.types.resale_authorization_product_name_filter

        out["ProductName"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_product_name_filter.serialize_json(
                value["product_name"]
            )
        )
    if "manufacturer_legal_name" in value:
        import aws_sdk_marketplace_catalog.types.resale_authorization_manufacturer_legal_name_filter

        out["ManufacturerLegalName"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_manufacturer_legal_name_filter.serialize_json(
                value["manufacturer_legal_name"]
            )
        )
    if "reseller_account_id" in value:
        import aws_sdk_marketplace_catalog.types.resale_authorization_reseller_account_id_filter

        out["ResellerAccountID"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_reseller_account_id_filter.serialize_json(
                value["reseller_account_id"]
            )
        )
    if "reseller_legal_name" in value:
        import aws_sdk_marketplace_catalog.types.resale_authorization_reseller_legal_name_filter

        out["ResellerLegalName"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_reseller_legal_name_filter.serialize_json(
                value["reseller_legal_name"]
            )
        )
    if "status" in value:
        import aws_sdk_marketplace_catalog.types.resale_authorization_status_filter

        out["Status"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_status_filter.serialize_json(
                value["status"]
            )
        )
    if "offer_extended_status" in value:
        import aws_sdk_marketplace_catalog.types.resale_authorization_offer_extended_status_filter

        out["OfferExtendedStatus"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_offer_extended_status_filter.serialize_json(
                value["offer_extended_status"]
            )
        )
    if "last_modified_date" in value:
        import aws_sdk_marketplace_catalog.types.resale_authorization_last_modified_date_filter

        out["LastModifiedDate"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_last_modified_date_filter.serialize_json(
                value["last_modified_date"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResaleAuthorizationFilters:
    out: ResaleAuthorizationFilters = {}  # type: ignore[typeddict-item]
    if "EntityId" in data:
        import aws_sdk_marketplace_catalog.types.resale_authorization_entity_id_filter

        out["entity_id"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_entity_id_filter.deserialize_json(
                data["EntityId"]
            )
        )
    if "Name" in data:
        import aws_sdk_marketplace_catalog.types.resale_authorization_name_filter

        out["name"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_name_filter.deserialize_json(
                data["Name"]
            )
        )
    if "ProductId" in data:
        import aws_sdk_marketplace_catalog.types.resale_authorization_product_id_filter

        out["product_id"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_product_id_filter.deserialize_json(
                data["ProductId"]
            )
        )
    if "CreatedDate" in data:
        import aws_sdk_marketplace_catalog.types.resale_authorization_created_date_filter

        out["created_date"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_created_date_filter.deserialize_json(
                data["CreatedDate"]
            )
        )
    if "AvailabilityEndDate" in data:
        import aws_sdk_marketplace_catalog.types.resale_authorization_availability_end_date_filter

        out["availability_end_date"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_availability_end_date_filter.deserialize_json(
                data["AvailabilityEndDate"]
            )
        )
    if "ManufacturerAccountId" in data:
        import aws_sdk_marketplace_catalog.types.resale_authorization_manufacturer_account_id_filter

        out["manufacturer_account_id"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_manufacturer_account_id_filter.deserialize_json(
                data["ManufacturerAccountId"]
            )
        )
    if "ProductName" in data:
        import aws_sdk_marketplace_catalog.types.resale_authorization_product_name_filter

        out["product_name"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_product_name_filter.deserialize_json(
                data["ProductName"]
            )
        )
    if "ManufacturerLegalName" in data:
        import aws_sdk_marketplace_catalog.types.resale_authorization_manufacturer_legal_name_filter

        out["manufacturer_legal_name"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_manufacturer_legal_name_filter.deserialize_json(
                data["ManufacturerLegalName"]
            )
        )
    if "ResellerAccountID" in data:
        import aws_sdk_marketplace_catalog.types.resale_authorization_reseller_account_id_filter

        out["reseller_account_id"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_reseller_account_id_filter.deserialize_json(
                data["ResellerAccountID"]
            )
        )
    if "ResellerLegalName" in data:
        import aws_sdk_marketplace_catalog.types.resale_authorization_reseller_legal_name_filter

        out["reseller_legal_name"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_reseller_legal_name_filter.deserialize_json(
                data["ResellerLegalName"]
            )
        )
    if "Status" in data:
        import aws_sdk_marketplace_catalog.types.resale_authorization_status_filter

        out["status"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_status_filter.deserialize_json(
                data["Status"]
            )
        )
    if "OfferExtendedStatus" in data:
        import aws_sdk_marketplace_catalog.types.resale_authorization_offer_extended_status_filter

        out["offer_extended_status"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_offer_extended_status_filter.deserialize_json(
                data["OfferExtendedStatus"]
            )
        )
    if "LastModifiedDate" in data:
        import aws_sdk_marketplace_catalog.types.resale_authorization_last_modified_date_filter

        out["last_modified_date"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_last_modified_date_filter.deserialize_json(
                data["LastModifiedDate"]
            )
        )
    return out
