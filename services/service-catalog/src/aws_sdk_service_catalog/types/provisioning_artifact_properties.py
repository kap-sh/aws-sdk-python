"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningArtifactProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.disable_template_validation
    import aws_sdk_service_catalog.types.provisioning_artifact_description
    import aws_sdk_service_catalog.types.provisioning_artifact_info
    import aws_sdk_service_catalog.types.provisioning_artifact_name
    import aws_sdk_service_catalog.types.provisioning_artifact_type


class ProvisioningArtifactProperties(TypedDict):
    name: NotRequired[
        "aws_sdk_service_catalog.types.provisioning_artifact_name.ProvisioningArtifactName"
    ]
    """<p>The name of the provisioning artifact (for example, v1 v2beta). No spaces are allowed.</p>"""
    description: NotRequired[
        "aws_sdk_service_catalog.types.provisioning_artifact_description.ProvisioningArtifactDescription"
    ]
    """<p>The description of the provisioning artifact, including how it differs from the previous provisioning artifact.</p>"""
    info: NotRequired[
        "aws_sdk_service_catalog.types.provisioning_artifact_info.ProvisioningArtifactInfo"
    ]
    """<p>Specify the template source with one of the following options, but not both. Keys accepted: [ <code>LoadTemplateFromURL</code>, <code>ImportFromPhysicalId</code> ]</p> <p>The URL of the CloudFormation template in Amazon S3 or GitHub in JSON format. Specify the URL in JSON format as follows:</p> <p> <code>\"LoadTemplateFromURL\": \"https://s3.amazonaws.com/cf-templates-ozkq9d3hgiq2-us-east-1/...\"</code> </p> <p> <code>ImportFromPhysicalId</code>: The physical id of the resource that contains the template. Currently only supports CloudFormation stack arn. Specify the physical id in JSON format as follows: <code>ImportFromPhysicalId: “arn:aws:cloudformation:[us-east-1]:[accountId]:stack/[StackName]/[resourceId]</code> </p>"""
    type: NotRequired[
        "aws_sdk_service_catalog.types.provisioning_artifact_type.ProvisioningArtifactType"
    ]
    """<p>The type of provisioning artifact.</p> <ul> <li> <p> <code>CLOUD_FORMATION_TEMPLATE</code> - CloudFormation template</p> </li> <li> <p> <code>TERRAFORM_OPEN_SOURCE</code> - Terraform Open Source configuration file</p> </li> <li> <p> <code>TERRAFORM_CLOUD</code> - Terraform Cloud configuration file</p> </li> <li> <p> <code>EXTERNAL</code> - External configuration file</p> </li> </ul>"""
    disable_template_validation: "aws_sdk_service_catalog.types.disable_template_validation.DisableTemplateValidation"
    """<p>If set to true, Service Catalog stops validating the specified provisioning artifact even if it is invalid. </p> <p>Service Catalog does not support template validation for the <code>TERRAFORM_OS</code> product type. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisioningArtifactProperties) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "info" in value:
        import aws_sdk_service_catalog.types.provisioning_artifact_info

        out["Info"] = (
            aws_sdk_service_catalog.types.provisioning_artifact_info.serialize_aws_json_1_1(
                value["info"]
            )
        )
    if "type" in value:
        import aws_sdk_service_catalog.types.provisioning_artifact_type

        out["Type"] = (
            aws_sdk_service_catalog.types.provisioning_artifact_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    out["DisableTemplateValidation"] = value.get("disable_template_validation", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvisioningArtifactProperties:
    out: ProvisioningArtifactProperties = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Info" in data:
        import aws_sdk_service_catalog.types.provisioning_artifact_info

        out["info"] = (
            aws_sdk_service_catalog.types.provisioning_artifact_info.deserialize_aws_json_1_1(
                data["Info"]
            )
        )
    if "Type" in data:
        import aws_sdk_service_catalog.types.provisioning_artifact_type

        out["type"] = (
            aws_sdk_service_catalog.types.provisioning_artifact_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "DisableTemplateValidation" in data:
        out["disable_template_validation"] = data["DisableTemplateValidation"]
    else:
        out["disable_template_validation"] = False
    return out
