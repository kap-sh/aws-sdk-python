"""Generated from Smithy shape ``com.amazonaws.servicecatalog#RecordDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.created_time
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.provisioned_product_name
    import aws_sdk_service_catalog.types.provisioned_product_type
    import aws_sdk_service_catalog.types.record_errors
    import aws_sdk_service_catalog.types.record_status
    import aws_sdk_service_catalog.types.record_tags
    import aws_sdk_service_catalog.types.record_type
    import aws_sdk_service_catalog.types.role_arn
    import aws_sdk_service_catalog.types.updated_time


class RecordDetail(TypedDict):
    record_id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The identifier of the record.</p>"""
    provisioned_product_name: NotRequired[
        "aws_sdk_service_catalog.types.provisioned_product_name.ProvisionedProductName"
    ]
    """<p>The user-friendly name of the provisioned product.</p>"""
    status: NotRequired["aws_sdk_service_catalog.types.record_status.RecordStatus"]
    """<p>The status of the provisioned product.</p> <ul> <li> <p> <code>CREATED</code> - The request was created but the operation has not started.</p> </li> <li> <p> <code>IN_PROGRESS</code> - The requested operation is in progress.</p> </li> <li> <p> <code>IN_PROGRESS_IN_ERROR</code> - The provisioned product is under change but the requested operation failed and some remediation is occurring. For example, a rollback.</p> </li> <li> <p> <code>SUCCEEDED</code> - The requested operation has successfully completed.</p> </li> <li> <p> <code>FAILED</code> - The requested operation has unsuccessfully completed. Investigate using the error messages returned.</p> </li> </ul>"""
    created_time: NotRequired["aws_sdk_service_catalog.types.created_time.CreatedTime"]
    """<p>The UTC time stamp of the creation time.</p>"""
    updated_time: NotRequired["aws_sdk_service_catalog.types.updated_time.UpdatedTime"]
    """<p>The time when the record was last updated.</p>"""
    provisioned_product_type: NotRequired[
        "aws_sdk_service_catalog.types.provisioned_product_type.ProvisionedProductType"
    ]
    """<p>The type of provisioned product. The supported values are <code>CFN_STACK</code>, <code>CFN_STACKSET</code>, <code>TERRAFORM_OPEN_SOURCE</code>, <code>TERRAFORM_CLOUD</code>, and <code>EXTERNAL</code>.</p>"""
    record_type: NotRequired["aws_sdk_service_catalog.types.record_type.RecordType"]
    """<p>The record type.</p> <ul> <li> <p> <code>PROVISION_PRODUCT</code> </p> </li> <li> <p> <code>UPDATE_PROVISIONED_PRODUCT</code> </p> </li> <li> <p> <code>TERMINATE_PROVISIONED_PRODUCT</code> </p> </li> </ul>"""
    provisioned_product_id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The identifier of the provisioned product.</p>"""
    product_id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The product identifier.</p>"""
    provisioning_artifact_id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The identifier of the provisioning artifact.</p>"""
    path_id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The path identifier.</p>"""
    record_errors: NotRequired[
        "aws_sdk_service_catalog.types.record_errors.RecordErrors"
    ]
    """<p>The errors that occurred.</p>"""
    record_tags: NotRequired["aws_sdk_service_catalog.types.record_tags.RecordTags"]
    """<p>One or more tags.</p>"""
    launch_role_arn: NotRequired["aws_sdk_service_catalog.types.role_arn.RoleArn"]
    """<p>The ARN of the launch role associated with the provisioned product.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordDetail) -> dict:
    out: dict = {}
    if "record_id" in value:
        out["RecordId"] = value["record_id"]
    if "provisioned_product_name" in value:
        out["ProvisionedProductName"] = value["provisioned_product_name"]
    if "status" in value:
        import aws_sdk_service_catalog.types.record_status

        out["Status"] = (
            aws_sdk_service_catalog.types.record_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "created_time" in value:
        import aws_sdk_service_catalog.types.created_time

        out["CreatedTime"] = (
            aws_sdk_service_catalog.types.created_time.serialize_aws_json_1_1(
                value["created_time"]
            )
        )
    if "updated_time" in value:
        import aws_sdk_service_catalog.types.updated_time

        out["UpdatedTime"] = (
            aws_sdk_service_catalog.types.updated_time.serialize_aws_json_1_1(
                value["updated_time"]
            )
        )
    if "provisioned_product_type" in value:
        out["ProvisionedProductType"] = value["provisioned_product_type"]
    if "record_type" in value:
        out["RecordType"] = value["record_type"]
    if "provisioned_product_id" in value:
        out["ProvisionedProductId"] = value["provisioned_product_id"]
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
    if "provisioning_artifact_id" in value:
        out["ProvisioningArtifactId"] = value["provisioning_artifact_id"]
    if "path_id" in value:
        out["PathId"] = value["path_id"]
    if "record_errors" in value:
        import aws_sdk_service_catalog.types.record_errors

        out["RecordErrors"] = (
            aws_sdk_service_catalog.types.record_errors.serialize_aws_json_1_1(
                value["record_errors"]
            )
        )
    if "record_tags" in value:
        import aws_sdk_service_catalog.types.record_tags

        out["RecordTags"] = (
            aws_sdk_service_catalog.types.record_tags.serialize_aws_json_1_1(
                value["record_tags"]
            )
        )
    if "launch_role_arn" in value:
        out["LaunchRoleArn"] = value["launch_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RecordDetail:
    out: RecordDetail = {}  # type: ignore[typeddict-item]
    if "RecordId" in data:
        out["record_id"] = data["RecordId"]
    if "ProvisionedProductName" in data:
        out["provisioned_product_name"] = data["ProvisionedProductName"]
    if "Status" in data:
        import aws_sdk_service_catalog.types.record_status

        out["status"] = (
            aws_sdk_service_catalog.types.record_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "CreatedTime" in data:
        import aws_sdk_service_catalog.types.created_time

        out["created_time"] = (
            aws_sdk_service_catalog.types.created_time.deserialize_aws_json_1_1(
                data["CreatedTime"]
            )
        )
    if "UpdatedTime" in data:
        import aws_sdk_service_catalog.types.updated_time

        out["updated_time"] = (
            aws_sdk_service_catalog.types.updated_time.deserialize_aws_json_1_1(
                data["UpdatedTime"]
            )
        )
    if "ProvisionedProductType" in data:
        out["provisioned_product_type"] = data["ProvisionedProductType"]
    if "RecordType" in data:
        out["record_type"] = data["RecordType"]
    if "ProvisionedProductId" in data:
        out["provisioned_product_id"] = data["ProvisionedProductId"]
    if "ProductId" in data:
        out["product_id"] = data["ProductId"]
    if "ProvisioningArtifactId" in data:
        out["provisioning_artifact_id"] = data["ProvisioningArtifactId"]
    if "PathId" in data:
        out["path_id"] = data["PathId"]
    if "RecordErrors" in data:
        import aws_sdk_service_catalog.types.record_errors

        out["record_errors"] = (
            aws_sdk_service_catalog.types.record_errors.deserialize_aws_json_1_1(
                data["RecordErrors"]
            )
        )
    if "RecordTags" in data:
        import aws_sdk_service_catalog.types.record_tags

        out["record_tags"] = (
            aws_sdk_service_catalog.types.record_tags.deserialize_aws_json_1_1(
                data["RecordTags"]
            )
        )
    if "LaunchRoleArn" in data:
        out["launch_role_arn"] = data["LaunchRoleArn"]
    return out
