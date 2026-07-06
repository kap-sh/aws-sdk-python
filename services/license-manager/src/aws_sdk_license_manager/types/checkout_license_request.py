"""Generated from Smithy shape ``com.amazonaws.licensemanager#CheckoutLicenseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.checkout_type
    import aws_sdk_license_manager.types.client_token
    import aws_sdk_license_manager.types.entitlement_data_list
    import aws_sdk_license_manager.types.string


class CheckoutLicenseRequest(TypedDict, closed=True):
    product_sku: "aws_sdk_license_manager.types.string.String"
    """<p>Product SKU.</p>"""
    checkout_type: "aws_sdk_license_manager.types.checkout_type.CheckoutType"
    """<p>Checkout type.</p>"""
    key_fingerprint: "aws_sdk_license_manager.types.string.String"
    """<p>Key fingerprint identifying the license.</p>"""
    entitlements: (
        "aws_sdk_license_manager.types.entitlement_data_list.EntitlementDataList"
    )
    """<p>License entitlements.</p>"""
    client_token: "aws_sdk_license_manager.types.client_token.ClientToken"
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    beneficiary: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>License beneficiary.</p>"""
    node_id: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Node ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CheckoutLicenseRequest) -> dict:
    out: dict = {}
    out["ProductSKU"] = value["product_sku"]
    import aws_sdk_license_manager.types.checkout_type

    out["CheckoutType"] = (
        aws_sdk_license_manager.types.checkout_type.serialize_aws_json_1_1(
            value["checkout_type"]
        )
    )
    out["KeyFingerprint"] = value["key_fingerprint"]
    import aws_sdk_license_manager.types.entitlement_data_list

    out["Entitlements"] = (
        aws_sdk_license_manager.types.entitlement_data_list.serialize_aws_json_1_1(
            value["entitlements"]
        )
    )
    out["ClientToken"] = value["client_token"]
    if "beneficiary" in value:
        out["Beneficiary"] = value["beneficiary"]
    if "node_id" in value:
        out["NodeId"] = value["node_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CheckoutLicenseRequest:
    out: CheckoutLicenseRequest = {}  # type: ignore[typeddict-item]
    if "ProductSKU" in data:
        out["product_sku"] = data["ProductSKU"]
    else:
        raise DeserializationError("CheckoutLicenseRequest.product_sku required")
    if "CheckoutType" in data:
        import aws_sdk_license_manager.types.checkout_type

        out["checkout_type"] = (
            aws_sdk_license_manager.types.checkout_type.deserialize_aws_json_1_1(
                data["CheckoutType"]
            )
        )
    else:
        raise DeserializationError("CheckoutLicenseRequest.checkout_type required")
    if "KeyFingerprint" in data:
        out["key_fingerprint"] = data["KeyFingerprint"]
    else:
        raise DeserializationError("CheckoutLicenseRequest.key_fingerprint required")
    if "Entitlements" in data:
        import aws_sdk_license_manager.types.entitlement_data_list

        out["entitlements"] = (
            aws_sdk_license_manager.types.entitlement_data_list.deserialize_aws_json_1_1(
                data["Entitlements"]
            )
        )
    else:
        raise DeserializationError("CheckoutLicenseRequest.entitlements required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError("CheckoutLicenseRequest.client_token required")
    if "Beneficiary" in data:
        out["beneficiary"] = data["Beneficiary"]
    if "NodeId" in data:
        out["node_id"] = data["NodeId"]
    return out
