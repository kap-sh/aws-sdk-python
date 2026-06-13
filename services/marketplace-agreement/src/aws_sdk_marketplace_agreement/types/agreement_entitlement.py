"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementEntitlement``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.agreement_entitlement_status
    import aws_sdk_marketplace_agreement.types.agreement_entitlement_status_reason_code
    import aws_sdk_marketplace_agreement.types.aws_arn
    import aws_sdk_marketplace_agreement.types.entitlement_type
    import aws_sdk_marketplace_agreement.types.registration_token
    import aws_sdk_marketplace_agreement.types.resource


class AgreementEntitlement(TypedDict):
    resource: NotRequired["aws_sdk_marketplace_agreement.types.resource.Resource"]
    """<p>The resource that the entitlement is provisioned to, such as a product.</p>"""
    type: NotRequired[
        "aws_sdk_marketplace_agreement.types.entitlement_type.EntitlementType"
    ]
    """<p>The type of entitlement.</p>"""
    registration_token: NotRequired[
        "aws_sdk_marketplace_agreement.types.registration_token.RegistrationToken"
    ]
    """<p>A short-lived token required by acceptors to register their account with the product provider. The token is only valid for 30 minutes after creation and is only applicable for purchase agreements.</p>"""
    status: NotRequired[
        "aws_sdk_marketplace_agreement.types.agreement_entitlement_status.AgreementEntitlementStatus"
    ]
    """<p>The current state of an entitlement.</p>"""
    status_reason_code: NotRequired[
        "aws_sdk_marketplace_agreement.types.agreement_entitlement_status_reason_code.AgreementEntitlementStatusReasonCode"
    ]
    """<p>Provides more information about the status of an entitlement.</p>"""
    license_arn: NotRequired["aws_sdk_marketplace_agreement.types.aws_arn.AwsArn"]
    """<p>The Amazon Resource Name (ARN) of the AWS License Manager license associated with the entitlement.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementEntitlement) -> dict:
    out: dict = {}
    if "resource" in value:
        import aws_sdk_marketplace_agreement.types.resource

        out["resource"] = (
            aws_sdk_marketplace_agreement.types.resource.serialize_aws_json_1_0(
                value["resource"]
            )
        )
    if "type" in value:
        out["type"] = value["type"]
    if "registration_token" in value:
        out["registrationToken"] = value["registration_token"]
    if "status" in value:
        import aws_sdk_marketplace_agreement.types.agreement_entitlement_status

        out["status"] = (
            aws_sdk_marketplace_agreement.types.agreement_entitlement_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "status_reason_code" in value:
        import aws_sdk_marketplace_agreement.types.agreement_entitlement_status_reason_code

        out["statusReasonCode"] = (
            aws_sdk_marketplace_agreement.types.agreement_entitlement_status_reason_code.serialize_aws_json_1_0(
                value["status_reason_code"]
            )
        )
    if "license_arn" in value:
        out["licenseArn"] = value["license_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AgreementEntitlement:
    out: AgreementEntitlement = {}  # type: ignore[typeddict-item]
    if "resource" in data:
        import aws_sdk_marketplace_agreement.types.resource

        out["resource"] = (
            aws_sdk_marketplace_agreement.types.resource.deserialize_aws_json_1_0(
                data["resource"]
            )
        )
    if "type" in data:
        out["type"] = data["type"]
    if "registrationToken" in data:
        out["registration_token"] = data["registrationToken"]
    if "status" in data:
        import aws_sdk_marketplace_agreement.types.agreement_entitlement_status

        out["status"] = (
            aws_sdk_marketplace_agreement.types.agreement_entitlement_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "statusReasonCode" in data:
        import aws_sdk_marketplace_agreement.types.agreement_entitlement_status_reason_code

        out["status_reason_code"] = (
            aws_sdk_marketplace_agreement.types.agreement_entitlement_status_reason_code.deserialize_aws_json_1_0(
                data["statusReasonCode"]
            )
        )
    if "licenseArn" in data:
        out["license_arn"] = data["licenseArn"]
    return out
