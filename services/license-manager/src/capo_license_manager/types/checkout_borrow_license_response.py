"""Generated from Smithy shape ``com.amazonaws.licensemanager#CheckoutBorrowLicenseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.arn
    import capo_license_manager.types.entitlement_data_list
    import capo_license_manager.types.iso8601_date_time
    import capo_license_manager.types.metadata_list
    import capo_license_manager.types.signed_token
    import capo_license_manager.types.string


class CheckoutBorrowLicenseResponse(TypedDict, closed=True):
    license_arn: NotRequired["capo_license_manager.types.arn.Arn"]
    """<p>Amazon Resource Name (ARN) of the license.</p>"""
    license_consumption_token: NotRequired["capo_license_manager.types.string.String"]
    """<p>License consumption token.</p>"""
    entitlements_allowed: NotRequired[
        "capo_license_manager.types.entitlement_data_list.EntitlementDataList"
    ]
    """<p>Allowed license entitlements.</p>"""
    node_id: NotRequired["capo_license_manager.types.string.String"]
    """<p>Node ID.</p>"""
    signed_token: NotRequired["capo_license_manager.types.signed_token.SignedToken"]
    """<p>Signed token.</p>"""
    issued_at: NotRequired[
        "capo_license_manager.types.iso8601_date_time.ISO8601DateTime"
    ]
    """<p>Date and time at which the license checkout is issued.</p>"""
    expiration: NotRequired[
        "capo_license_manager.types.iso8601_date_time.ISO8601DateTime"
    ]
    """<p>Date and time at which the license checkout expires.</p>"""
    checkout_metadata: NotRequired[
        "capo_license_manager.types.metadata_list.MetadataList"
    ]
    """<p>Information about constraints.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CheckoutBorrowLicenseResponse) -> dict:
    out: dict = {}
    if "license_arn" in value:
        out["LicenseArn"] = value["license_arn"]
    if "license_consumption_token" in value:
        out["LicenseConsumptionToken"] = value["license_consumption_token"]
    if "entitlements_allowed" in value:
        import capo_license_manager.types.entitlement_data_list

        out["EntitlementsAllowed"] = (
            capo_license_manager.types.entitlement_data_list.serialize_aws_json_1_1(
                value["entitlements_allowed"]
            )
        )
    if "node_id" in value:
        out["NodeId"] = value["node_id"]
    if "signed_token" in value:
        out["SignedToken"] = value["signed_token"]
    if "issued_at" in value:
        out["IssuedAt"] = value["issued_at"]
    if "expiration" in value:
        out["Expiration"] = value["expiration"]
    if "checkout_metadata" in value:
        import capo_license_manager.types.metadata_list

        out["CheckoutMetadata"] = (
            capo_license_manager.types.metadata_list.serialize_aws_json_1_1(
                value["checkout_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CheckoutBorrowLicenseResponse:
    out: CheckoutBorrowLicenseResponse = {}  # type: ignore[typeddict-item]
    if "LicenseArn" in data:
        out["license_arn"] = data["LicenseArn"]
    if "LicenseConsumptionToken" in data:
        out["license_consumption_token"] = data["LicenseConsumptionToken"]
    if "EntitlementsAllowed" in data:
        import capo_license_manager.types.entitlement_data_list

        out["entitlements_allowed"] = (
            capo_license_manager.types.entitlement_data_list.deserialize_aws_json_1_1(
                data["EntitlementsAllowed"]
            )
        )
    if "NodeId" in data:
        out["node_id"] = data["NodeId"]
    if "SignedToken" in data:
        out["signed_token"] = data["SignedToken"]
    if "IssuedAt" in data:
        out["issued_at"] = data["IssuedAt"]
    if "Expiration" in data:
        out["expiration"] = data["Expiration"]
    if "CheckoutMetadata" in data:
        import capo_license_manager.types.metadata_list

        out["checkout_metadata"] = (
            capo_license_manager.types.metadata_list.deserialize_aws_json_1_1(
                data["CheckoutMetadata"]
            )
        )
    return out
