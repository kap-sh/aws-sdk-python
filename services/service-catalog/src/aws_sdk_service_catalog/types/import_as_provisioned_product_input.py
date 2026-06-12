"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ImportAsProvisionedProductInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.accept_language
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.idempotency_token
    import aws_sdk_service_catalog.types.physical_id
    import aws_sdk_service_catalog.types.provisioned_product_name


class ImportAsProvisionedProductInput(TypedDict):
    accept_language: NotRequired[
        "aws_sdk_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    product_id: "aws_sdk_service_catalog.types.id.Id"
    """<p>The product identifier.</p>"""
    provisioning_artifact_id: "aws_sdk_service_catalog.types.id.Id"
    """<p>The identifier of the provisioning artifact.</p>"""
    provisioned_product_name: (
        "aws_sdk_service_catalog.types.provisioned_product_name.ProvisionedProductName"
    )
    """<p>The user-friendly name of the provisioned product. The value must be unique for the Amazon Web Services account. The name cannot be updated after the product is provisioned. </p>"""
    physical_id: "aws_sdk_service_catalog.types.physical_id.PhysicalId"
    """<p>The unique identifier of the resource to be imported. It only currently supports CloudFormation stack IDs.</p>"""
    idempotency_token: (
        "aws_sdk_service_catalog.types.idempotency_token.IdempotencyToken"
    )
    """<p>A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportAsProvisionedProductInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["ProductId"] = value["product_id"]
    out["ProvisioningArtifactId"] = value["provisioning_artifact_id"]
    out["ProvisionedProductName"] = value["provisioned_product_name"]
    out["PhysicalId"] = value["physical_id"]
    out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportAsProvisionedProductInput:
    out: ImportAsProvisionedProductInput = {}  # type: ignore[typeddict-item]
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    if "ProductId" in data:
        out["product_id"] = data["ProductId"]
    else:
        raise DeserializationError(
            "ImportAsProvisionedProductInput.product_id required"
        )
    if "ProvisioningArtifactId" in data:
        out["provisioning_artifact_id"] = data["ProvisioningArtifactId"]
    else:
        raise DeserializationError(
            "ImportAsProvisionedProductInput.provisioning_artifact_id required"
        )
    if "ProvisionedProductName" in data:
        out["provisioned_product_name"] = data["ProvisionedProductName"]
    else:
        raise DeserializationError(
            "ImportAsProvisionedProductInput.provisioned_product_name required"
        )
    if "PhysicalId" in data:
        out["physical_id"] = data["PhysicalId"]
    else:
        raise DeserializationError(
            "ImportAsProvisionedProductInput.physical_id required"
        )
    if "IdempotencyToken" in data:
        out["idempotency_token"] = data["IdempotencyToken"]
    else:
        raise DeserializationError(
            "ImportAsProvisionedProductInput.idempotency_token required"
        )
    return out
