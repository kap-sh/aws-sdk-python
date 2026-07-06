"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CreateProvisionedProductPlanInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.accept_language
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.idempotency_token
    import aws_sdk_service_catalog.types.notification_arns
    import aws_sdk_service_catalog.types.provisioned_product_name
    import aws_sdk_service_catalog.types.provisioned_product_plan_name
    import aws_sdk_service_catalog.types.provisioned_product_plan_type
    import aws_sdk_service_catalog.types.tags
    import aws_sdk_service_catalog.types.update_provisioning_parameters


class CreateProvisionedProductPlanInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "aws_sdk_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    plan_name: "aws_sdk_service_catalog.types.provisioned_product_plan_name.ProvisionedProductPlanName"
    """<p>The name of the plan.</p>"""
    plan_type: "aws_sdk_service_catalog.types.provisioned_product_plan_type.ProvisionedProductPlanType"
    """<p>The plan type.</p>"""
    notification_arns: NotRequired[
        "aws_sdk_service_catalog.types.notification_arns.NotificationArns"
    ]
    """<p>Passed to CloudFormation. The SNS topic ARNs to which to publish stack-related events.</p>"""
    path_id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use <a>ListLaunchPaths</a>.</p>"""
    product_id: "aws_sdk_service_catalog.types.id.Id"
    """<p>The product identifier.</p>"""
    provisioned_product_name: (
        "aws_sdk_service_catalog.types.provisioned_product_name.ProvisionedProductName"
    )
    """<p>A user-friendly name for the provisioned product. This value must be unique for the Amazon Web Services account and cannot be updated after the product is provisioned.</p>"""
    provisioning_artifact_id: "aws_sdk_service_catalog.types.id.Id"
    """<p>The identifier of the provisioning artifact.</p>"""
    provisioning_parameters: NotRequired[
        "aws_sdk_service_catalog.types.update_provisioning_parameters.UpdateProvisioningParameters"
    ]
    """<p>Parameters specified by the administrator that are required for provisioning the product.</p>"""
    idempotency_token: (
        "aws_sdk_service_catalog.types.idempotency_token.IdempotencyToken"
    )
    """<p>A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.</p>"""
    tags: NotRequired["aws_sdk_service_catalog.types.tags.Tags"]
    """<p>One or more tags.</p> <p>If the plan is for an existing provisioned product, the product must have a <code>RESOURCE_UPDATE</code> constraint with <code>TagUpdatesOnProvisionedProduct</code> set to <code>ALLOWED</code> to allow tag updates.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateProvisionedProductPlanInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["PlanName"] = value["plan_name"]
    import aws_sdk_service_catalog.types.provisioned_product_plan_type

    out["PlanType"] = (
        aws_sdk_service_catalog.types.provisioned_product_plan_type.serialize_aws_json_1_1(
            value["plan_type"]
        )
    )
    if "notification_arns" in value:
        import aws_sdk_service_catalog.types.notification_arns

        out["NotificationArns"] = (
            aws_sdk_service_catalog.types.notification_arns.serialize_aws_json_1_1(
                value["notification_arns"]
            )
        )
    if "path_id" in value:
        out["PathId"] = value["path_id"]
    out["ProductId"] = value["product_id"]
    out["ProvisionedProductName"] = value["provisioned_product_name"]
    out["ProvisioningArtifactId"] = value["provisioning_artifact_id"]
    if "provisioning_parameters" in value:
        import aws_sdk_service_catalog.types.update_provisioning_parameters

        out["ProvisioningParameters"] = (
            aws_sdk_service_catalog.types.update_provisioning_parameters.serialize_aws_json_1_1(
                value["provisioning_parameters"]
            )
        )
    out["IdempotencyToken"] = value["idempotency_token"]
    if "tags" in value:
        import aws_sdk_service_catalog.types.tags

        out["Tags"] = aws_sdk_service_catalog.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateProvisionedProductPlanInput:
    out: CreateProvisionedProductPlanInput = {}  # type: ignore[typeddict-item]
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    if "PlanName" in data:
        out["plan_name"] = data["PlanName"]
    else:
        raise DeserializationError(
            "CreateProvisionedProductPlanInput.plan_name required"
        )
    if "PlanType" in data:
        import aws_sdk_service_catalog.types.provisioned_product_plan_type

        out["plan_type"] = (
            aws_sdk_service_catalog.types.provisioned_product_plan_type.deserialize_aws_json_1_1(
                data["PlanType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateProvisionedProductPlanInput.plan_type required"
        )
    if "NotificationArns" in data:
        import aws_sdk_service_catalog.types.notification_arns

        out["notification_arns"] = (
            aws_sdk_service_catalog.types.notification_arns.deserialize_aws_json_1_1(
                data["NotificationArns"]
            )
        )
    if "PathId" in data:
        out["path_id"] = data["PathId"]
    if "ProductId" in data:
        out["product_id"] = data["ProductId"]
    else:
        raise DeserializationError(
            "CreateProvisionedProductPlanInput.product_id required"
        )
    if "ProvisionedProductName" in data:
        out["provisioned_product_name"] = data["ProvisionedProductName"]
    else:
        raise DeserializationError(
            "CreateProvisionedProductPlanInput.provisioned_product_name required"
        )
    if "ProvisioningArtifactId" in data:
        out["provisioning_artifact_id"] = data["ProvisioningArtifactId"]
    else:
        raise DeserializationError(
            "CreateProvisionedProductPlanInput.provisioning_artifact_id required"
        )
    if "ProvisioningParameters" in data:
        import aws_sdk_service_catalog.types.update_provisioning_parameters

        out["provisioning_parameters"] = (
            aws_sdk_service_catalog.types.update_provisioning_parameters.deserialize_aws_json_1_1(
                data["ProvisioningParameters"]
            )
        )
    if "IdempotencyToken" in data:
        out["idempotency_token"] = data["IdempotencyToken"]
    else:
        raise DeserializationError(
            "CreateProvisionedProductPlanInput.idempotency_token required"
        )
    if "Tags" in data:
        import aws_sdk_service_catalog.types.tags

        out["tags"] = aws_sdk_service_catalog.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
