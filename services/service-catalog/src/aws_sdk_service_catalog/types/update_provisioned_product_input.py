"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UpdateProvisionedProductInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.accept_language
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.idempotency_token
    import aws_sdk_service_catalog.types.portfolio_display_name
    import aws_sdk_service_catalog.types.product_view_name
    import aws_sdk_service_catalog.types.provisioned_product_name_or_arn
    import aws_sdk_service_catalog.types.provisioning_artifact_name
    import aws_sdk_service_catalog.types.tags
    import aws_sdk_service_catalog.types.update_provisioning_parameters
    import aws_sdk_service_catalog.types.update_provisioning_preferences


class UpdateProvisionedProductInput(TypedDict):
    accept_language: NotRequired[
        "aws_sdk_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    provisioned_product_name: NotRequired[
        "aws_sdk_service_catalog.types.provisioned_product_name_or_arn.ProvisionedProductNameOrArn"
    ]
    """<p>The name of the provisioned product. You cannot specify both <code>ProvisionedProductName</code> and <code>ProvisionedProductId</code>.</p>"""
    provisioned_product_id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The identifier of the provisioned product. You must provide the name or ID, but not both.</p>"""
    product_id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The identifier of the product. You must provide the name or ID, but not both.</p>"""
    product_name: NotRequired[
        "aws_sdk_service_catalog.types.product_view_name.ProductViewName"
    ]
    """<p>The name of the product. You must provide the name or ID, but not both.</p>"""
    provisioning_artifact_id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The identifier of the provisioning artifact.</p>"""
    provisioning_artifact_name: NotRequired[
        "aws_sdk_service_catalog.types.provisioning_artifact_name.ProvisioningArtifactName"
    ]
    """<p>The name of the provisioning artifact. You must provide the name or ID, but not both.</p>"""
    path_id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The path identifier. This value is optional if the product has a default path, and required if the product has more than one path. You must provide the name or ID, but not both.</p>"""
    path_name: NotRequired[
        "aws_sdk_service_catalog.types.portfolio_display_name.PortfolioDisplayName"
    ]
    """<p>The name of the path. You must provide the name or ID, but not both.</p>"""
    provisioning_parameters: NotRequired[
        "aws_sdk_service_catalog.types.update_provisioning_parameters.UpdateProvisioningParameters"
    ]
    """<p>The new parameters.</p>"""
    provisioning_preferences: NotRequired[
        "aws_sdk_service_catalog.types.update_provisioning_preferences.UpdateProvisioningPreferences"
    ]
    """<p>An object that contains information about the provisioning preferences for a stack set.</p>"""
    tags: NotRequired["aws_sdk_service_catalog.types.tags.Tags"]
    """<p>One or more tags. Requires the product to have <code>RESOURCE_UPDATE</code> constraint with <code>TagUpdatesOnProvisionedProduct</code> set to <code>ALLOWED</code> to allow tag updates.</p>"""
    update_token: "aws_sdk_service_catalog.types.idempotency_token.IdempotencyToken"
    """<p>The idempotency token that uniquely identifies the provisioning update request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProvisionedProductInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    if "provisioned_product_name" in value:
        out["ProvisionedProductName"] = value["provisioned_product_name"]
    if "provisioned_product_id" in value:
        out["ProvisionedProductId"] = value["provisioned_product_id"]
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
    if "product_name" in value:
        out["ProductName"] = value["product_name"]
    if "provisioning_artifact_id" in value:
        out["ProvisioningArtifactId"] = value["provisioning_artifact_id"]
    if "provisioning_artifact_name" in value:
        out["ProvisioningArtifactName"] = value["provisioning_artifact_name"]
    if "path_id" in value:
        out["PathId"] = value["path_id"]
    if "path_name" in value:
        out["PathName"] = value["path_name"]
    if "provisioning_parameters" in value:
        import aws_sdk_service_catalog.types.update_provisioning_parameters

        out["ProvisioningParameters"] = (
            aws_sdk_service_catalog.types.update_provisioning_parameters.serialize_aws_json_1_1(
                value["provisioning_parameters"]
            )
        )
    if "provisioning_preferences" in value:
        import aws_sdk_service_catalog.types.update_provisioning_preferences

        out["ProvisioningPreferences"] = (
            aws_sdk_service_catalog.types.update_provisioning_preferences.serialize_aws_json_1_1(
                value["provisioning_preferences"]
            )
        )
    if "tags" in value:
        import aws_sdk_service_catalog.types.tags

        out["Tags"] = aws_sdk_service_catalog.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    out["UpdateToken"] = value["update_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProvisionedProductInput:
    out: UpdateProvisionedProductInput = {}  # type: ignore[typeddict-item]
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    if "ProvisionedProductName" in data:
        out["provisioned_product_name"] = data["ProvisionedProductName"]
    if "ProvisionedProductId" in data:
        out["provisioned_product_id"] = data["ProvisionedProductId"]
    if "ProductId" in data:
        out["product_id"] = data["ProductId"]
    if "ProductName" in data:
        out["product_name"] = data["ProductName"]
    if "ProvisioningArtifactId" in data:
        out["provisioning_artifact_id"] = data["ProvisioningArtifactId"]
    if "ProvisioningArtifactName" in data:
        out["provisioning_artifact_name"] = data["ProvisioningArtifactName"]
    if "PathId" in data:
        out["path_id"] = data["PathId"]
    if "PathName" in data:
        out["path_name"] = data["PathName"]
    if "ProvisioningParameters" in data:
        import aws_sdk_service_catalog.types.update_provisioning_parameters

        out["provisioning_parameters"] = (
            aws_sdk_service_catalog.types.update_provisioning_parameters.deserialize_aws_json_1_1(
                data["ProvisioningParameters"]
            )
        )
    if "ProvisioningPreferences" in data:
        import aws_sdk_service_catalog.types.update_provisioning_preferences

        out["provisioning_preferences"] = (
            aws_sdk_service_catalog.types.update_provisioning_preferences.deserialize_aws_json_1_1(
                data["ProvisioningPreferences"]
            )
        )
    if "Tags" in data:
        import aws_sdk_service_catalog.types.tags

        out["tags"] = aws_sdk_service_catalog.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "UpdateToken" in data:
        out["update_token"] = data["UpdateToken"]
    else:
        raise DeserializationError(
            "UpdateProvisionedProductInput.update_token required"
        )
    return out
