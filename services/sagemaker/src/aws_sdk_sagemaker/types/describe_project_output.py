"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeProjectOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.entity_description
    import aws_sdk_sagemaker.types.project_arn
    import aws_sdk_sagemaker.types.project_entity_name
    import aws_sdk_sagemaker.types.project_id
    import aws_sdk_sagemaker.types.project_status
    import aws_sdk_sagemaker.types.service_catalog_provisioned_product_details
    import aws_sdk_sagemaker.types.service_catalog_provisioning_details
    import aws_sdk_sagemaker.types.template_provider_detail_list
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.user_context


class DescribeProjectOutput(TypedDict):
    project_arn: NotRequired["aws_sdk_sagemaker.types.project_arn.ProjectArn"]
    """<p>The Amazon Resource Name (ARN) of the project.</p>"""
    project_name: NotRequired[
        "aws_sdk_sagemaker.types.project_entity_name.ProjectEntityName"
    ]
    """<p>The name of the project.</p>"""
    project_id: NotRequired["aws_sdk_sagemaker.types.project_id.ProjectId"]
    """<p>The ID of the project.</p>"""
    project_description: NotRequired[
        "aws_sdk_sagemaker.types.entity_description.EntityDescription"
    ]
    """<p>The description of the project.</p>"""
    service_catalog_provisioning_details: NotRequired[
        "aws_sdk_sagemaker.types.service_catalog_provisioning_details.ServiceCatalogProvisioningDetails"
    ]
    """<p>Information used to provision a service catalog product. For information, see <a href=\"https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html\">What is Amazon Web Services Service Catalog</a>.</p>"""
    service_catalog_provisioned_product_details: NotRequired[
        "aws_sdk_sagemaker.types.service_catalog_provisioned_product_details.ServiceCatalogProvisionedProductDetails"
    ]
    """<p>Information about a provisioned service catalog product.</p>"""
    project_status: NotRequired["aws_sdk_sagemaker.types.project_status.ProjectStatus"]
    """<p>The status of the project.</p>"""
    template_provider_details: NotRequired[
        "aws_sdk_sagemaker.types.template_provider_detail_list.TemplateProviderDetailList"
    ]
    """<p> An array of template providers associated with the project. </p>"""
    created_by: NotRequired["aws_sdk_sagemaker.types.user_context.UserContext"]
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the project was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp when project was last modified.</p>"""
    last_modified_by: NotRequired["aws_sdk_sagemaker.types.user_context.UserContext"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProjectOutput) -> dict:
    out: dict = {}
    if "project_arn" in value:
        out["ProjectArn"] = value["project_arn"]
    if "project_name" in value:
        out["ProjectName"] = value["project_name"]
    if "project_id" in value:
        out["ProjectId"] = value["project_id"]
    if "project_description" in value:
        out["ProjectDescription"] = value["project_description"]
    if "service_catalog_provisioning_details" in value:
        import aws_sdk_sagemaker.types.service_catalog_provisioning_details

        out["ServiceCatalogProvisioningDetails"] = (
            aws_sdk_sagemaker.types.service_catalog_provisioning_details.serialize_aws_json_1_1(
                value["service_catalog_provisioning_details"]
            )
        )
    if "service_catalog_provisioned_product_details" in value:
        import aws_sdk_sagemaker.types.service_catalog_provisioned_product_details

        out["ServiceCatalogProvisionedProductDetails"] = (
            aws_sdk_sagemaker.types.service_catalog_provisioned_product_details.serialize_aws_json_1_1(
                value["service_catalog_provisioned_product_details"]
            )
        )
    if "project_status" in value:
        import aws_sdk_sagemaker.types.project_status

        out["ProjectStatus"] = (
            aws_sdk_sagemaker.types.project_status.serialize_aws_json_1_1(
                value["project_status"]
            )
        )
    if "template_provider_details" in value:
        import aws_sdk_sagemaker.types.template_provider_detail_list

        out["TemplateProviderDetails"] = (
            aws_sdk_sagemaker.types.template_provider_detail_list.serialize_aws_json_1_1(
                value["template_provider_details"]
            )
        )
    if "created_by" in value:
        import aws_sdk_sagemaker.types.user_context

        out["CreatedBy"] = aws_sdk_sagemaker.types.user_context.serialize_aws_json_1_1(
            value["created_by"]
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "last_modified_by" in value:
        import aws_sdk_sagemaker.types.user_context

        out["LastModifiedBy"] = (
            aws_sdk_sagemaker.types.user_context.serialize_aws_json_1_1(
                value["last_modified_by"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProjectOutput:
    out: DescribeProjectOutput = {}  # type: ignore[typeddict-item]
    if "ProjectArn" in data:
        out["project_arn"] = data["ProjectArn"]
    if "ProjectName" in data:
        out["project_name"] = data["ProjectName"]
    if "ProjectId" in data:
        out["project_id"] = data["ProjectId"]
    if "ProjectDescription" in data:
        out["project_description"] = data["ProjectDescription"]
    if "ServiceCatalogProvisioningDetails" in data:
        import aws_sdk_sagemaker.types.service_catalog_provisioning_details

        out["service_catalog_provisioning_details"] = (
            aws_sdk_sagemaker.types.service_catalog_provisioning_details.deserialize_aws_json_1_1(
                data["ServiceCatalogProvisioningDetails"]
            )
        )
    if "ServiceCatalogProvisionedProductDetails" in data:
        import aws_sdk_sagemaker.types.service_catalog_provisioned_product_details

        out["service_catalog_provisioned_product_details"] = (
            aws_sdk_sagemaker.types.service_catalog_provisioned_product_details.deserialize_aws_json_1_1(
                data["ServiceCatalogProvisionedProductDetails"]
            )
        )
    if "ProjectStatus" in data:
        import aws_sdk_sagemaker.types.project_status

        out["project_status"] = (
            aws_sdk_sagemaker.types.project_status.deserialize_aws_json_1_1(
                data["ProjectStatus"]
            )
        )
    if "TemplateProviderDetails" in data:
        import aws_sdk_sagemaker.types.template_provider_detail_list

        out["template_provider_details"] = (
            aws_sdk_sagemaker.types.template_provider_detail_list.deserialize_aws_json_1_1(
                data["TemplateProviderDetails"]
            )
        )
    if "CreatedBy" in data:
        import aws_sdk_sagemaker.types.user_context

        out["created_by"] = (
            aws_sdk_sagemaker.types.user_context.deserialize_aws_json_1_1(
                data["CreatedBy"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "LastModifiedBy" in data:
        import aws_sdk_sagemaker.types.user_context

        out["last_modified_by"] = (
            aws_sdk_sagemaker.types.user_context.deserialize_aws_json_1_1(
                data["LastModifiedBy"]
            )
        )
    return out
