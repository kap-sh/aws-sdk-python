"""Generated from Smithy shape ``com.amazonaws.sagemaker#ServiceCatalogProvisioningUpdateDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.provisioning_parameters
    import aws_sdk_sagemaker.types.service_catalog_entity_id


class ServiceCatalogProvisioningUpdateDetails(TypedDict, closed=True):
    provisioning_artifact_id: NotRequired[
        "aws_sdk_sagemaker.types.service_catalog_entity_id.ServiceCatalogEntityId"
    ]
    """<p>The ID of the provisioning artifact.</p>"""
    provisioning_parameters: NotRequired[
        "aws_sdk_sagemaker.types.provisioning_parameters.ProvisioningParameters"
    ]
    """<p>A list of key value pairs that you specify when you provision a product.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceCatalogProvisioningUpdateDetails) -> dict:
    out: dict = {}
    if "provisioning_artifact_id" in value:
        out["ProvisioningArtifactId"] = value["provisioning_artifact_id"]
    if "provisioning_parameters" in value:
        import aws_sdk_sagemaker.types.provisioning_parameters

        out["ProvisioningParameters"] = (
            aws_sdk_sagemaker.types.provisioning_parameters.serialize_aws_json_1_1(
                value["provisioning_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceCatalogProvisioningUpdateDetails:
    out: ServiceCatalogProvisioningUpdateDetails = {}  # type: ignore[typeddict-item]
    if "ProvisioningArtifactId" in data:
        out["provisioning_artifact_id"] = data["ProvisioningArtifactId"]
    if "ProvisioningParameters" in data:
        import aws_sdk_sagemaker.types.provisioning_parameters

        out["provisioning_parameters"] = (
            aws_sdk_sagemaker.types.provisioning_parameters.deserialize_aws_json_1_1(
                data["ProvisioningParameters"]
            )
        )
    return out
