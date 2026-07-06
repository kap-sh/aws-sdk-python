"""Generated from Smithy shape ``com.amazonaws.sagemaker#ServiceCatalogProvisionedProductDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.provisioned_product_status_message
    import aws_sdk_sagemaker.types.service_catalog_entity_id


class ServiceCatalogProvisionedProductDetails(TypedDict, closed=True):
    provisioned_product_id: NotRequired[
        "aws_sdk_sagemaker.types.service_catalog_entity_id.ServiceCatalogEntityId"
    ]
    """<p>The ID of the provisioned product.</p>"""
    provisioned_product_status_message: NotRequired[
        "aws_sdk_sagemaker.types.provisioned_product_status_message.ProvisionedProductStatusMessage"
    ]
    """<p>The current status of the product.</p> <ul> <li> <p> <code>AVAILABLE</code> - Stable state, ready to perform any operation. The most recent operation succeeded and completed.</p> </li> <li> <p> <code>UNDER_CHANGE</code> - Transitive state. Operations performed might not have valid results. Wait for an AVAILABLE status before performing operations.</p> </li> <li> <p> <code>TAINTED</code> - Stable state, ready to perform any operation. The stack has completed the requested operation but is not exactly what was requested. For example, a request to update to a new version failed and the stack rolled back to the current version.</p> </li> <li> <p> <code>ERROR</code> - An unexpected error occurred. The provisioned product exists but the stack is not running. For example, CloudFormation received a parameter value that was not valid and could not launch the stack.</p> </li> <li> <p> <code>PLAN_IN_PROGRESS</code> - Transitive state. The plan operations were performed to provision a new product, but resources have not yet been created. After reviewing the list of resources to be created, execute the plan. Wait for an AVAILABLE status before performing operations.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceCatalogProvisionedProductDetails) -> dict:
    out: dict = {}
    if "provisioned_product_id" in value:
        out["ProvisionedProductId"] = value["provisioned_product_id"]
    if "provisioned_product_status_message" in value:
        out["ProvisionedProductStatusMessage"] = value[
            "provisioned_product_status_message"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceCatalogProvisionedProductDetails:
    out: ServiceCatalogProvisionedProductDetails = {}  # type: ignore[typeddict-item]
    if "ProvisionedProductId" in data:
        out["provisioned_product_id"] = data["ProvisionedProductId"]
    if "ProvisionedProductStatusMessage" in data:
        out["provisioned_product_status_message"] = data[
            "ProvisionedProductStatusMessage"
        ]
    return out
