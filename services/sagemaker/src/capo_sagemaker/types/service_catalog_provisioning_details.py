"""Generated from Smithy shape ``com.amazonaws.sagemaker#ServiceCatalogProvisioningDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.provisioning_parameters
    import capo_sagemaker.types.service_catalog_entity_id


class ServiceCatalogProvisioningDetails(TypedDict, closed=True):
    product_id: NotRequired[
        "capo_sagemaker.types.service_catalog_entity_id.ServiceCatalogEntityId"
    ]
    """<p>The ID of the product to provision.</p>"""
    provisioning_artifact_id: NotRequired[
        "capo_sagemaker.types.service_catalog_entity_id.ServiceCatalogEntityId"
    ]
    """<p>The ID of the provisioning artifact.</p>"""
    path_id: NotRequired[
        "capo_sagemaker.types.service_catalog_entity_id.ServiceCatalogEntityId"
    ]
    """<p>The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path. </p>"""
    provisioning_parameters: NotRequired[
        "capo_sagemaker.types.provisioning_parameters.ProvisioningParameters"
    ]
    """<p>A list of key value pairs that you specify when you provision a product.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceCatalogProvisioningDetails) -> dict:
    out: dict = {}
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
    if "provisioning_artifact_id" in value:
        out["ProvisioningArtifactId"] = value["provisioning_artifact_id"]
    if "path_id" in value:
        out["PathId"] = value["path_id"]
    if "provisioning_parameters" in value:
        import capo_sagemaker.types.provisioning_parameters

        out["ProvisioningParameters"] = (
            capo_sagemaker.types.provisioning_parameters.serialize_aws_json_1_1(
                value["provisioning_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceCatalogProvisioningDetails:
    out: ServiceCatalogProvisioningDetails = {}  # type: ignore[typeddict-item]
    if "ProductId" in data:
        out["product_id"] = data["ProductId"]
    if "ProvisioningArtifactId" in data:
        out["provisioning_artifact_id"] = data["ProvisioningArtifactId"]
    if "PathId" in data:
        out["path_id"] = data["PathId"]
    if "ProvisioningParameters" in data:
        import capo_sagemaker.types.provisioning_parameters

        out["provisioning_parameters"] = (
            capo_sagemaker.types.provisioning_parameters.deserialize_aws_json_1_1(
                data["ProvisioningParameters"]
            )
        )
    return out
