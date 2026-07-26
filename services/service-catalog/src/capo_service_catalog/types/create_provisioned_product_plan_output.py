"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CreateProvisionedProductPlanOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.id
    import capo_service_catalog.types.provisioned_product_name
    import capo_service_catalog.types.provisioned_product_plan_name


class CreateProvisionedProductPlanOutput(TypedDict, closed=True):
    plan_name: NotRequired[
        "capo_service_catalog.types.provisioned_product_plan_name.ProvisionedProductPlanName"
    ]
    """<p>The name of the plan.</p>"""
    plan_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The plan identifier.</p>"""
    provision_product_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The product identifier.</p>"""
    provisioned_product_name: NotRequired[
        "capo_service_catalog.types.provisioned_product_name.ProvisionedProductName"
    ]
    """<p>The user-friendly name of the provisioned product.</p>"""
    provisioning_artifact_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The identifier of the provisioning artifact.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateProvisionedProductPlanOutput) -> dict:
    out: dict = {}
    if "plan_name" in value:
        out["PlanName"] = value["plan_name"]
    if "plan_id" in value:
        out["PlanId"] = value["plan_id"]
    if "provision_product_id" in value:
        out["ProvisionProductId"] = value["provision_product_id"]
    if "provisioned_product_name" in value:
        out["ProvisionedProductName"] = value["provisioned_product_name"]
    if "provisioning_artifact_id" in value:
        out["ProvisioningArtifactId"] = value["provisioning_artifact_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateProvisionedProductPlanOutput:
    out: CreateProvisionedProductPlanOutput = {}  # type: ignore[typeddict-item]
    if "PlanName" in data:
        out["plan_name"] = data["PlanName"]
    if "PlanId" in data:
        out["plan_id"] = data["PlanId"]
    if "ProvisionProductId" in data:
        out["provision_product_id"] = data["ProvisionProductId"]
    if "ProvisionedProductName" in data:
        out["provisioned_product_name"] = data["ProvisionedProductName"]
    if "ProvisioningArtifactId" in data:
        out["provisioning_artifact_id"] = data["ProvisioningArtifactId"]
    return out
