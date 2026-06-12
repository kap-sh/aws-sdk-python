"""Generated from Smithy shape ``com.amazonaws.servicecatalog#TerminateProvisionedProductInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.accept_language
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.idempotency_token
    import aws_sdk_service_catalog.types.ignore_errors
    import aws_sdk_service_catalog.types.provisioned_product_name_or_arn
    import aws_sdk_service_catalog.types.retain_physical_resources


class TerminateProvisionedProductInput(TypedDict):
    provisioned_product_name: NotRequired[
        "aws_sdk_service_catalog.types.provisioned_product_name_or_arn.ProvisionedProductNameOrArn"
    ]
    """<p>The name of the provisioned product. You cannot specify both <code>ProvisionedProductName</code> and <code>ProvisionedProductId</code>.</p>"""
    provisioned_product_id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The identifier of the provisioned product. You cannot specify both <code>ProvisionedProductName</code> and <code>ProvisionedProductId</code>.</p>"""
    terminate_token: "aws_sdk_service_catalog.types.idempotency_token.IdempotencyToken"
    """<p>An idempotency token that uniquely identifies the termination request. This token is only valid during the termination process. After the provisioned product is terminated, subsequent requests to terminate the same provisioned product always return <b>ResourceNotFound</b>.</p>"""
    ignore_errors: "aws_sdk_service_catalog.types.ignore_errors.IgnoreErrors"
    """<p>If set to true, Service Catalog stops managing the specified provisioned product even if it cannot delete the underlying resources.</p>"""
    accept_language: NotRequired[
        "aws_sdk_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    retain_physical_resources: "aws_sdk_service_catalog.types.retain_physical_resources.RetainPhysicalResources"
    """<p>When this boolean parameter is set to true, the <code>TerminateProvisionedProduct</code> API deletes the Service Catalog provisioned product. However, it does not remove the CloudFormation stack, stack set, or the underlying resources of the deleted provisioned product. The default value is false.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminateProvisionedProductInput) -> dict:
    out: dict = {}
    if "provisioned_product_name" in value:
        out["ProvisionedProductName"] = value["provisioned_product_name"]
    if "provisioned_product_id" in value:
        out["ProvisionedProductId"] = value["provisioned_product_id"]
    out["TerminateToken"] = value["terminate_token"]
    out["IgnoreErrors"] = value.get("ignore_errors", False)
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["RetainPhysicalResources"] = value.get("retain_physical_resources", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> TerminateProvisionedProductInput:
    out: TerminateProvisionedProductInput = {}  # type: ignore[typeddict-item]
    if "ProvisionedProductName" in data:
        out["provisioned_product_name"] = data["ProvisionedProductName"]
    if "ProvisionedProductId" in data:
        out["provisioned_product_id"] = data["ProvisionedProductId"]
    if "TerminateToken" in data:
        out["terminate_token"] = data["TerminateToken"]
    else:
        raise DeserializationError(
            "TerminateProvisionedProductInput.terminate_token required"
        )
    if "IgnoreErrors" in data:
        out["ignore_errors"] = data["IgnoreErrors"]
    else:
        out["ignore_errors"] = False
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    if "RetainPhysicalResources" in data:
        out["retain_physical_resources"] = data["RetainPhysicalResources"]
    else:
        out["retain_physical_resources"] = False
    return out
