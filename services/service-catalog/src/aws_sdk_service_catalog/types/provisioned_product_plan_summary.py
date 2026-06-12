"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisionedProductPlanSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.provisioned_product_name
    import aws_sdk_service_catalog.types.provisioned_product_plan_name
    import aws_sdk_service_catalog.types.provisioned_product_plan_type


class ProvisionedProductPlanSummary(TypedDict):
    plan_name: NotRequired[
        "aws_sdk_service_catalog.types.provisioned_product_plan_name.ProvisionedProductPlanName"
    ]
    """<p>The name of the plan.</p>"""
    plan_id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The plan identifier.</p>"""
    provision_product_id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The product identifier.</p>"""
    provision_product_name: NotRequired[
        "aws_sdk_service_catalog.types.provisioned_product_name.ProvisionedProductName"
    ]
    """<p>The user-friendly name of the provisioned product.</p>"""
    plan_type: NotRequired[
        "aws_sdk_service_catalog.types.provisioned_product_plan_type.ProvisionedProductPlanType"
    ]
    """<p>The plan type.</p>"""
    provisioning_artifact_id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The identifier of the provisioning artifact.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisionedProductPlanSummary) -> dict:
    out: dict = {}
    if "plan_name" in value:
        out["PlanName"] = value["plan_name"]
    if "plan_id" in value:
        out["PlanId"] = value["plan_id"]
    if "provision_product_id" in value:
        out["ProvisionProductId"] = value["provision_product_id"]
    if "provision_product_name" in value:
        out["ProvisionProductName"] = value["provision_product_name"]
    if "plan_type" in value:
        import aws_sdk_service_catalog.types.provisioned_product_plan_type

        out["PlanType"] = (
            aws_sdk_service_catalog.types.provisioned_product_plan_type.serialize_aws_json_1_1(
                value["plan_type"]
            )
        )
    if "provisioning_artifact_id" in value:
        out["ProvisioningArtifactId"] = value["provisioning_artifact_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvisionedProductPlanSummary:
    out: ProvisionedProductPlanSummary = {}  # type: ignore[typeddict-item]
    if "PlanName" in data:
        out["plan_name"] = data["PlanName"]
    if "PlanId" in data:
        out["plan_id"] = data["PlanId"]
    if "ProvisionProductId" in data:
        out["provision_product_id"] = data["ProvisionProductId"]
    if "ProvisionProductName" in data:
        out["provision_product_name"] = data["ProvisionProductName"]
    if "PlanType" in data:
        import aws_sdk_service_catalog.types.provisioned_product_plan_type

        out["plan_type"] = (
            aws_sdk_service_catalog.types.provisioned_product_plan_type.deserialize_aws_json_1_1(
                data["PlanType"]
            )
        )
    if "ProvisioningArtifactId" in data:
        out["provisioning_artifact_id"] = data["ProvisioningArtifactId"]
    return out
