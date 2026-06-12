"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResaleAuthorizationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.date_time_iso8601
    import aws_sdk_marketplace_catalog.types.resale_authorization_manufacturer_account_id_string
    import aws_sdk_marketplace_catalog.types.resale_authorization_manufacturer_legal_name_string
    import aws_sdk_marketplace_catalog.types.resale_authorization_name_string
    import aws_sdk_marketplace_catalog.types.resale_authorization_offer_extended_status_string
    import aws_sdk_marketplace_catalog.types.resale_authorization_product_id_string
    import aws_sdk_marketplace_catalog.types.resale_authorization_product_name_string
    import aws_sdk_marketplace_catalog.types.resale_authorization_reseller_account_id_string
    import aws_sdk_marketplace_catalog.types.resale_authorization_reseller_legal_name_string
    import aws_sdk_marketplace_catalog.types.resale_authorization_status_string


class ResaleAuthorizationSummary(TypedDict):
    name: NotRequired[
        "aws_sdk_marketplace_catalog.types.resale_authorization_name_string.ResaleAuthorizationNameString"
    ]
    """<p>The name of the ResaleAuthorization.</p>"""
    product_id: NotRequired[
        "aws_sdk_marketplace_catalog.types.resale_authorization_product_id_string.ResaleAuthorizationProductIdString"
    ]
    """<p>The product ID of the ResaleAuthorization.</p>"""
    product_name: NotRequired[
        "aws_sdk_marketplace_catalog.types.resale_authorization_product_name_string.ResaleAuthorizationProductNameString"
    ]
    """<p>The product name of the ResaleAuthorization.</p>"""
    manufacturer_account_id: NotRequired[
        "aws_sdk_marketplace_catalog.types.resale_authorization_manufacturer_account_id_string.ResaleAuthorizationManufacturerAccountIdString"
    ]
    """<p>The manufacturer account ID of the ResaleAuthorization.</p>"""
    manufacturer_legal_name: NotRequired[
        "aws_sdk_marketplace_catalog.types.resale_authorization_manufacturer_legal_name_string.ResaleAuthorizationManufacturerLegalNameString"
    ]
    """<p>The manufacturer legal name of the ResaleAuthorization.</p>"""
    reseller_account_id: NotRequired[
        "aws_sdk_marketplace_catalog.types.resale_authorization_reseller_account_id_string.ResaleAuthorizationResellerAccountIDString"
    ]
    """<p>The reseller account ID of the ResaleAuthorization.</p>"""
    reseller_legal_name: NotRequired[
        "aws_sdk_marketplace_catalog.types.resale_authorization_reseller_legal_name_string.ResaleAuthorizationResellerLegalNameString"
    ]
    """<p>The reseller legal name of the ResaleAuthorization</p>"""
    status: NotRequired[
        "aws_sdk_marketplace_catalog.types.resale_authorization_status_string.ResaleAuthorizationStatusString"
    ]
    """<p>The status of the ResaleAuthorization.</p>"""
    offer_extended_status: NotRequired[
        "aws_sdk_marketplace_catalog.types.resale_authorization_offer_extended_status_string.ResaleAuthorizationOfferExtendedStatusString"
    ]
    """<p>The offer extended status of the ResaleAuthorization</p>"""
    created_date: NotRequired[
        "aws_sdk_marketplace_catalog.types.date_time_iso8601.DateTimeISO8601"
    ]
    """<p>The created date of the ResaleAuthorization.</p>"""
    availability_end_date: NotRequired[
        "aws_sdk_marketplace_catalog.types.date_time_iso8601.DateTimeISO8601"
    ]
    """<p>The availability end date of the ResaleAuthorization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResaleAuthorizationSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
    if "product_name" in value:
        out["ProductName"] = value["product_name"]
    if "manufacturer_account_id" in value:
        out["ManufacturerAccountId"] = value["manufacturer_account_id"]
    if "manufacturer_legal_name" in value:
        out["ManufacturerLegalName"] = value["manufacturer_legal_name"]
    if "reseller_account_id" in value:
        out["ResellerAccountID"] = value["reseller_account_id"]
    if "reseller_legal_name" in value:
        out["ResellerLegalName"] = value["reseller_legal_name"]
    if "status" in value:
        import aws_sdk_marketplace_catalog.types.resale_authorization_status_string

        out["Status"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_status_string.serialize_json(
                value["status"]
            )
        )
    if "offer_extended_status" in value:
        out["OfferExtendedStatus"] = value["offer_extended_status"]
    if "created_date" in value:
        out["CreatedDate"] = value["created_date"]
    if "availability_end_date" in value:
        out["AvailabilityEndDate"] = value["availability_end_date"]
    return out


def deserialize_json(data: dict) -> ResaleAuthorizationSummary:
    out: ResaleAuthorizationSummary = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ProductId" in data:
        out["product_id"] = data["ProductId"]
    if "ProductName" in data:
        out["product_name"] = data["ProductName"]
    if "ManufacturerAccountId" in data:
        out["manufacturer_account_id"] = data["ManufacturerAccountId"]
    if "ManufacturerLegalName" in data:
        out["manufacturer_legal_name"] = data["ManufacturerLegalName"]
    if "ResellerAccountID" in data:
        out["reseller_account_id"] = data["ResellerAccountID"]
    if "ResellerLegalName" in data:
        out["reseller_legal_name"] = data["ResellerLegalName"]
    if "Status" in data:
        import aws_sdk_marketplace_catalog.types.resale_authorization_status_string

        out["status"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_status_string.deserialize_json(
                data["Status"]
            )
        )
    if "OfferExtendedStatus" in data:
        out["offer_extended_status"] = data["OfferExtendedStatus"]
    if "CreatedDate" in data:
        out["created_date"] = data["CreatedDate"]
    if "AvailabilityEndDate" in data:
        out["availability_end_date"] = data["AvailabilityEndDate"]
    return out
