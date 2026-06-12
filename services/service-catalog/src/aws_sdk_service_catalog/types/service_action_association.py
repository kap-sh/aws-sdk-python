"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ServiceActionAssociation``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.id


class ServiceActionAssociation(TypedDict):
    service_action_id: "aws_sdk_service_catalog.types.id.Id"
    """<p>The self-service action identifier. For example, <code>act-fs7abcd89wxyz</code>.</p>"""
    product_id: "aws_sdk_service_catalog.types.id.Id"
    """<p>The product identifier. For example, <code>prod-abcdzk7xy33qa</code>.</p>"""
    provisioning_artifact_id: "aws_sdk_service_catalog.types.id.Id"
    """<p>The identifier of the provisioning artifact. For example, <code>pa-4abcdjnxjj6ne</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceActionAssociation) -> dict:
    out: dict = {}
    out["ServiceActionId"] = value["service_action_id"]
    out["ProductId"] = value["product_id"]
    out["ProvisioningArtifactId"] = value["provisioning_artifact_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceActionAssociation:
    out: ServiceActionAssociation = {}  # type: ignore[typeddict-item]
    if "ServiceActionId" in data:
        out["service_action_id"] = data["ServiceActionId"]
    else:
        raise DeserializationError(
            "ServiceActionAssociation.service_action_id required"
        )
    if "ProductId" in data:
        out["product_id"] = data["ProductId"]
    else:
        raise DeserializationError("ServiceActionAssociation.product_id required")
    if "ProvisioningArtifactId" in data:
        out["provisioning_artifact_id"] = data["ProvisioningArtifactId"]
    else:
        raise DeserializationError(
            "ServiceActionAssociation.provisioning_artifact_id required"
        )
    return out
