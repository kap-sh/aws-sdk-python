"""Generated from Smithy shape ``com.amazonaws.licensemanager#CheckoutLicenseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.checkout_type
    import capo_license_manager.types.entitlement_data_list
    import capo_license_manager.types.iso8601_date_time
    import capo_license_manager.types.signed_token
    import capo_license_manager.types.string


class CheckoutLicenseResponse(TypedDict, closed=True):
    checkout_type: NotRequired["capo_license_manager.types.checkout_type.CheckoutType"]
    """<p>Checkout type.</p>"""
    license_consumption_token: NotRequired["capo_license_manager.types.string.String"]
    """<p>License consumption token.</p>"""
    entitlements_allowed: NotRequired[
        "capo_license_manager.types.entitlement_data_list.EntitlementDataList"
    ]
    """<p>Allowed license entitlements.</p>"""
    signed_token: NotRequired["capo_license_manager.types.signed_token.SignedToken"]
    """<p>Signed token.</p>"""
    node_id: NotRequired["capo_license_manager.types.string.String"]
    """<p>Node ID.</p>"""
    issued_at: NotRequired[
        "capo_license_manager.types.iso8601_date_time.ISO8601DateTime"
    ]
    """<p>Date and time at which the license checkout is issued.</p>"""
    expiration: NotRequired[
        "capo_license_manager.types.iso8601_date_time.ISO8601DateTime"
    ]
    """<p>Date and time at which the license checkout expires.</p>"""
    license_arn: NotRequired["capo_license_manager.types.string.String"]
    """<p>Amazon Resource Name (ARN) of the checkout license.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CheckoutLicenseResponse) -> dict:
    out: dict = {}
    if "checkout_type" in value:
        import capo_license_manager.types.checkout_type

        out["CheckoutType"] = (
            capo_license_manager.types.checkout_type.serialize_aws_json_1_1(
                value["checkout_type"]
            )
        )
    if "license_consumption_token" in value:
        out["LicenseConsumptionToken"] = value["license_consumption_token"]
    if "entitlements_allowed" in value:
        import capo_license_manager.types.entitlement_data_list

        out["EntitlementsAllowed"] = (
            capo_license_manager.types.entitlement_data_list.serialize_aws_json_1_1(
                value["entitlements_allowed"]
            )
        )
    if "signed_token" in value:
        out["SignedToken"] = value["signed_token"]
    if "node_id" in value:
        out["NodeId"] = value["node_id"]
    if "issued_at" in value:
        out["IssuedAt"] = value["issued_at"]
    if "expiration" in value:
        out["Expiration"] = value["expiration"]
    if "license_arn" in value:
        out["LicenseArn"] = value["license_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CheckoutLicenseResponse:
    out: CheckoutLicenseResponse = {}  # type: ignore[typeddict-item]
    if "CheckoutType" in data:
        import capo_license_manager.types.checkout_type

        out["checkout_type"] = (
            capo_license_manager.types.checkout_type.deserialize_aws_json_1_1(
                data["CheckoutType"]
            )
        )
    if "LicenseConsumptionToken" in data:
        out["license_consumption_token"] = data["LicenseConsumptionToken"]
    if "EntitlementsAllowed" in data:
        import capo_license_manager.types.entitlement_data_list

        out["entitlements_allowed"] = (
            capo_license_manager.types.entitlement_data_list.deserialize_aws_json_1_1(
                data["EntitlementsAllowed"]
            )
        )
    if "SignedToken" in data:
        out["signed_token"] = data["SignedToken"]
    if "NodeId" in data:
        out["node_id"] = data["NodeId"]
    if "IssuedAt" in data:
        out["issued_at"] = data["IssuedAt"]
    if "Expiration" in data:
        out["expiration"] = data["Expiration"]
    if "LicenseArn" in data:
        out["license_arn"] = data["LicenseArn"]
    return out
