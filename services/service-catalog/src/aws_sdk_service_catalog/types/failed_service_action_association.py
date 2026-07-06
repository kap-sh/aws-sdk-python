"""Generated from Smithy shape ``com.amazonaws.servicecatalog#FailedServiceActionAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.service_action_association_error_code
    import aws_sdk_service_catalog.types.service_action_association_error_message


class FailedServiceActionAssociation(TypedDict, closed=True):
    service_action_id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The self-service action identifier. For example, <code>act-fs7abcd89wxyz</code>.</p>"""
    product_id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The product identifier. For example, <code>prod-abcdzk7xy33qa</code>.</p>"""
    provisioning_artifact_id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The identifier of the provisioning artifact. For example, <code>pa-4abcdjnxjj6ne</code>.</p>"""
    error_code: NotRequired[
        "aws_sdk_service_catalog.types.service_action_association_error_code.ServiceActionAssociationErrorCode"
    ]
    """<p>The error code. Valid values are listed below.</p>"""
    error_message: NotRequired[
        "aws_sdk_service_catalog.types.service_action_association_error_message.ServiceActionAssociationErrorMessage"
    ]
    """<p>A text description of the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedServiceActionAssociation) -> dict:
    out: dict = {}
    if "service_action_id" in value:
        out["ServiceActionId"] = value["service_action_id"]
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
    if "provisioning_artifact_id" in value:
        out["ProvisioningArtifactId"] = value["provisioning_artifact_id"]
    if "error_code" in value:
        import aws_sdk_service_catalog.types.service_action_association_error_code

        out["ErrorCode"] = (
            aws_sdk_service_catalog.types.service_action_association_error_code.serialize_aws_json_1_1(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FailedServiceActionAssociation:
    out: FailedServiceActionAssociation = {}  # type: ignore[typeddict-item]
    if "ServiceActionId" in data:
        out["service_action_id"] = data["ServiceActionId"]
    if "ProductId" in data:
        out["product_id"] = data["ProductId"]
    if "ProvisioningArtifactId" in data:
        out["provisioning_artifact_id"] = data["ProvisioningArtifactId"]
    if "ErrorCode" in data:
        import aws_sdk_service_catalog.types.service_action_association_error_code

        out["error_code"] = (
            aws_sdk_service_catalog.types.service_action_association_error_code.deserialize_aws_json_1_1(
                data["ErrorCode"]
            )
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
