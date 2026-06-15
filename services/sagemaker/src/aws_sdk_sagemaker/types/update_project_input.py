"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateProjectInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.entity_description
    import aws_sdk_sagemaker.types.project_entity_name
    import aws_sdk_sagemaker.types.service_catalog_provisioning_update_details
    import aws_sdk_sagemaker.types.tag_list
    import aws_sdk_sagemaker.types.update_template_provider_list


class UpdateProjectInput(TypedDict):
    project_name: NotRequired[
        "aws_sdk_sagemaker.types.project_entity_name.ProjectEntityName"
    ]
    """<p>The name of the project.</p>"""
    project_description: NotRequired[
        "aws_sdk_sagemaker.types.entity_description.EntityDescription"
    ]
    """<p>The description for the project.</p>"""
    service_catalog_provisioning_update_details: NotRequired[
        "aws_sdk_sagemaker.types.service_catalog_provisioning_update_details.ServiceCatalogProvisioningUpdateDetails"
    ]
    r"""<p>The product ID and provisioning artifact ID to provision a service catalog. The provisioning artifact ID will default to the latest provisioning artifact ID of the product, if you don't provide the provisioning artifact ID. For more information, see <a href=\"https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html\">What is Amazon Web Services Service Catalog</a>. </p>"""
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    r"""<p>An array of key-value pairs. You can use tags to categorize your Amazon Web Services resources in different ways, for example, by purpose, owner, or environment. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services Resources</a>. In addition, the project must have tag update constraints set in order to include this parameter in the request. For more information, see <a href=\"https://docs.aws.amazon.com/servicecatalog/latest/adminguide/constraints-resourceupdate.html\">Amazon Web Services Service Catalog Tag Update Constraints</a>.</p>"""
    template_providers_to_update: NotRequired[
        "aws_sdk_sagemaker.types.update_template_provider_list.UpdateTemplateProviderList"
    ]
    """<p> The template providers to update in the project. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProjectInput) -> dict:
    out: dict = {}
    if "project_name" in value:
        out["ProjectName"] = value["project_name"]
    if "project_description" in value:
        out["ProjectDescription"] = value["project_description"]
    if "service_catalog_provisioning_update_details" in value:
        import aws_sdk_sagemaker.types.service_catalog_provisioning_update_details

        out["ServiceCatalogProvisioningUpdateDetails"] = (
            aws_sdk_sagemaker.types.service_catalog_provisioning_update_details.serialize_aws_json_1_1(
                value["service_catalog_provisioning_update_details"]
            )
        )
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "template_providers_to_update" in value:
        import aws_sdk_sagemaker.types.update_template_provider_list

        out["TemplateProvidersToUpdate"] = (
            aws_sdk_sagemaker.types.update_template_provider_list.serialize_aws_json_1_1(
                value["template_providers_to_update"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProjectInput:
    out: UpdateProjectInput = {}  # type: ignore[typeddict-item]
    if "ProjectName" in data:
        out["project_name"] = data["ProjectName"]
    if "ProjectDescription" in data:
        out["project_description"] = data["ProjectDescription"]
    if "ServiceCatalogProvisioningUpdateDetails" in data:
        import aws_sdk_sagemaker.types.service_catalog_provisioning_update_details

        out["service_catalog_provisioning_update_details"] = (
            aws_sdk_sagemaker.types.service_catalog_provisioning_update_details.deserialize_aws_json_1_1(
                data["ServiceCatalogProvisioningUpdateDetails"]
            )
        )
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "TemplateProvidersToUpdate" in data:
        import aws_sdk_sagemaker.types.update_template_provider_list

        out["template_providers_to_update"] = (
            aws_sdk_sagemaker.types.update_template_provider_list.deserialize_aws_json_1_1(
                data["TemplateProvidersToUpdate"]
            )
        )
    return out
