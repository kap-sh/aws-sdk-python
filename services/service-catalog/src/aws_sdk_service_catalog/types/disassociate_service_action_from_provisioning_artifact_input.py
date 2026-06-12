"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DisassociateServiceActionFromProvisioningArtifactInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.accept_language
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.idempotency_token


class DisassociateServiceActionFromProvisioningArtifactInput(TypedDict):
    product_id: "aws_sdk_service_catalog.types.id.Id"
    """<p>The product identifier. For example, <code>prod-abcdzk7xy33qa</code>.</p>"""
    provisioning_artifact_id: "aws_sdk_service_catalog.types.id.Id"
    """<p>The identifier of the provisioning artifact. For example, <code>pa-4abcdjnxjj6ne</code>.</p>"""
    service_action_id: "aws_sdk_service_catalog.types.id.Id"
    """<p>The self-service action identifier. For example, <code>act-fs7abcd89wxyz</code>.</p>"""
    accept_language: NotRequired[
        "aws_sdk_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    idempotency_token: NotRequired[
        "aws_sdk_service_catalog.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique identifier that you provide to ensure idempotency. If multiple requests from the same Amazon Web Services account use the same idempotency token, the same response is returned for each repeated request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DisassociateServiceActionFromProvisioningArtifactInput,
) -> dict:
    out: dict = {}
    out["ProductId"] = value["product_id"]
    out["ProvisioningArtifactId"] = value["provisioning_artifact_id"]
    out["ServiceActionId"] = value["service_action_id"]
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DisassociateServiceActionFromProvisioningArtifactInput:
    out: DisassociateServiceActionFromProvisioningArtifactInput = {}  # type: ignore[typeddict-item]
    if "ProductId" in data:
        out["product_id"] = data["ProductId"]
    else:
        raise DeserializationError(
            "DisassociateServiceActionFromProvisioningArtifactInput.product_id required"
        )
    if "ProvisioningArtifactId" in data:
        out["provisioning_artifact_id"] = data["ProvisioningArtifactId"]
    else:
        raise DeserializationError(
            "DisassociateServiceActionFromProvisioningArtifactInput.provisioning_artifact_id required"
        )
    if "ServiceActionId" in data:
        out["service_action_id"] = data["ServiceActionId"]
    else:
        raise DeserializationError(
            "DisassociateServiceActionFromProvisioningArtifactInput.service_action_id required"
        )
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    if "IdempotencyToken" in data:
        out["idempotency_token"] = data["IdempotencyToken"]
    return out
