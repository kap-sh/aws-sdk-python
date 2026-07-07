"""Generated from Smithy shape ``com.amazonaws.licensemanager#CheckoutBorrowLicenseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.arn
    import aws_sdk_license_manager.types.client_token
    import aws_sdk_license_manager.types.digital_signature_method
    import aws_sdk_license_manager.types.entitlement_data_list
    import aws_sdk_license_manager.types.metadata_list
    import aws_sdk_license_manager.types.string


class CheckoutBorrowLicenseRequest(TypedDict, closed=True):
    license_arn: "aws_sdk_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the license. The license must use the borrow consumption configuration.</p>"""
    entitlements: (
        "aws_sdk_license_manager.types.entitlement_data_list.EntitlementDataList"
    )
    """<p>License entitlements. Partial checkouts are not supported.</p>"""
    digital_signature_method: (
        "aws_sdk_license_manager.types.digital_signature_method.DigitalSignatureMethod"
    )
    r"""<p>Digital signature method. The possible value is JSON Web Signature (JWS) algorithm PS384. For more information, see <a href=\"https://tools.ietf.org/html/rfc7518#section-3.5\">RFC 7518 Digital Signature with RSASSA-PSS</a>.</p>"""
    node_id: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Node ID.</p>"""
    checkout_metadata: NotRequired[
        "aws_sdk_license_manager.types.metadata_list.MetadataList"
    ]
    """<p>Information about constraints.</p>"""
    client_token: "aws_sdk_license_manager.types.client_token.ClientToken"
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CheckoutBorrowLicenseRequest) -> dict:
    out: dict = {}
    out["LicenseArn"] = value["license_arn"]
    import aws_sdk_license_manager.types.entitlement_data_list

    out["Entitlements"] = (
        aws_sdk_license_manager.types.entitlement_data_list.serialize_aws_json_1_1(
            value["entitlements"]
        )
    )
    import aws_sdk_license_manager.types.digital_signature_method

    out["DigitalSignatureMethod"] = (
        aws_sdk_license_manager.types.digital_signature_method.serialize_aws_json_1_1(
            value["digital_signature_method"]
        )
    )
    if "node_id" in value:
        out["NodeId"] = value["node_id"]
    if "checkout_metadata" in value:
        import aws_sdk_license_manager.types.metadata_list

        out["CheckoutMetadata"] = (
            aws_sdk_license_manager.types.metadata_list.serialize_aws_json_1_1(
                value["checkout_metadata"]
            )
        )
    out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CheckoutBorrowLicenseRequest:
    out: CheckoutBorrowLicenseRequest = {}  # type: ignore[typeddict-item]
    if "LicenseArn" in data:
        out["license_arn"] = data["LicenseArn"]
    else:
        raise DeserializationError("CheckoutBorrowLicenseRequest.license_arn required")
    if "Entitlements" in data:
        import aws_sdk_license_manager.types.entitlement_data_list

        out["entitlements"] = (
            aws_sdk_license_manager.types.entitlement_data_list.deserialize_aws_json_1_1(
                data["Entitlements"]
            )
        )
    else:
        raise DeserializationError("CheckoutBorrowLicenseRequest.entitlements required")
    if "DigitalSignatureMethod" in data:
        import aws_sdk_license_manager.types.digital_signature_method

        out["digital_signature_method"] = (
            aws_sdk_license_manager.types.digital_signature_method.deserialize_aws_json_1_1(
                data["DigitalSignatureMethod"]
            )
        )
    else:
        raise DeserializationError(
            "CheckoutBorrowLicenseRequest.digital_signature_method required"
        )
    if "NodeId" in data:
        out["node_id"] = data["NodeId"]
    if "CheckoutMetadata" in data:
        import aws_sdk_license_manager.types.metadata_list

        out["checkout_metadata"] = (
            aws_sdk_license_manager.types.metadata_list.deserialize_aws_json_1_1(
                data["CheckoutMetadata"]
            )
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError("CheckoutBorrowLicenseRequest.client_token required")
    return out
