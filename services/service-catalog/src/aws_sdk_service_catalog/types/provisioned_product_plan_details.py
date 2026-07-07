"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisionedProductPlanDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.created_time
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.notification_arns
    import aws_sdk_service_catalog.types.provisioned_product_name
    import aws_sdk_service_catalog.types.provisioned_product_plan_name
    import aws_sdk_service_catalog.types.provisioned_product_plan_status
    import aws_sdk_service_catalog.types.provisioned_product_plan_type
    import aws_sdk_service_catalog.types.status_message
    import aws_sdk_service_catalog.types.tags
    import aws_sdk_service_catalog.types.update_provisioning_parameters
    import aws_sdk_service_catalog.types.updated_time


class ProvisionedProductPlanDetails(TypedDict, closed=True):
    created_time: NotRequired["aws_sdk_service_catalog.types.created_time.CreatedTime"]
    """<p>The UTC time stamp of the creation time.</p>"""
    path_id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use <a>ListLaunchPaths</a>.</p>"""
    product_id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The product identifier.</p>"""
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
    status: NotRequired[
        "aws_sdk_service_catalog.types.provisioned_product_plan_status.ProvisionedProductPlanStatus"
    ]
    """<p>The status.</p>"""
    updated_time: NotRequired["aws_sdk_service_catalog.types.updated_time.UpdatedTime"]
    """<p>The UTC time stamp when the plan was last updated.</p>"""
    notification_arns: NotRequired[
        "aws_sdk_service_catalog.types.notification_arns.NotificationArns"
    ]
    """<p>Passed to CloudFormation. The SNS topic ARNs to which to publish stack-related events.</p>"""
    provisioning_parameters: NotRequired[
        "aws_sdk_service_catalog.types.update_provisioning_parameters.UpdateProvisioningParameters"
    ]
    """<p>Parameters specified by the administrator that are required for provisioning the product.</p>"""
    tags: NotRequired["aws_sdk_service_catalog.types.tags.Tags"]
    """<p>One or more tags.</p>"""
    status_message: NotRequired[
        "aws_sdk_service_catalog.types.status_message.StatusMessage"
    ]
    """<p>The status message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisionedProductPlanDetails) -> dict:
    out: dict = {}
    if "created_time" in value:
        import aws_sdk_service_catalog.types.created_time

        out["CreatedTime"] = (
            aws_sdk_service_catalog.types.created_time.serialize_aws_json_1_1(
                value["created_time"]
            )
        )
    if "path_id" in value:
        out["PathId"] = value["path_id"]
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
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
    if "status" in value:
        import aws_sdk_service_catalog.types.provisioned_product_plan_status

        out["Status"] = (
            aws_sdk_service_catalog.types.provisioned_product_plan_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "updated_time" in value:
        import aws_sdk_service_catalog.types.updated_time

        out["UpdatedTime"] = (
            aws_sdk_service_catalog.types.updated_time.serialize_aws_json_1_1(
                value["updated_time"]
            )
        )
    if "notification_arns" in value:
        import aws_sdk_service_catalog.types.notification_arns

        out["NotificationArns"] = (
            aws_sdk_service_catalog.types.notification_arns.serialize_aws_json_1_1(
                value["notification_arns"]
            )
        )
    if "provisioning_parameters" in value:
        import aws_sdk_service_catalog.types.update_provisioning_parameters

        out["ProvisioningParameters"] = (
            aws_sdk_service_catalog.types.update_provisioning_parameters.serialize_aws_json_1_1(
                value["provisioning_parameters"]
            )
        )
    if "tags" in value:
        import aws_sdk_service_catalog.types.tags

        out["Tags"] = aws_sdk_service_catalog.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvisionedProductPlanDetails:
    out: ProvisionedProductPlanDetails = {}  # type: ignore[typeddict-item]
    if "CreatedTime" in data:
        import aws_sdk_service_catalog.types.created_time

        out["created_time"] = (
            aws_sdk_service_catalog.types.created_time.deserialize_aws_json_1_1(
                data["CreatedTime"]
            )
        )
    if "PathId" in data:
        out["path_id"] = data["PathId"]
    if "ProductId" in data:
        out["product_id"] = data["ProductId"]
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
    if "Status" in data:
        import aws_sdk_service_catalog.types.provisioned_product_plan_status

        out["status"] = (
            aws_sdk_service_catalog.types.provisioned_product_plan_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "UpdatedTime" in data:
        import aws_sdk_service_catalog.types.updated_time

        out["updated_time"] = (
            aws_sdk_service_catalog.types.updated_time.deserialize_aws_json_1_1(
                data["UpdatedTime"]
            )
        )
    if "NotificationArns" in data:
        import aws_sdk_service_catalog.types.notification_arns

        out["notification_arns"] = (
            aws_sdk_service_catalog.types.notification_arns.deserialize_aws_json_1_1(
                data["NotificationArns"]
            )
        )
    if "ProvisioningParameters" in data:
        import aws_sdk_service_catalog.types.update_provisioning_parameters

        out["provisioning_parameters"] = (
            aws_sdk_service_catalog.types.update_provisioning_parameters.deserialize_aws_json_1_1(
                data["ProvisioningParameters"]
            )
        )
    if "Tags" in data:
        import aws_sdk_service_catalog.types.tags

        out["tags"] = aws_sdk_service_catalog.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    return out
