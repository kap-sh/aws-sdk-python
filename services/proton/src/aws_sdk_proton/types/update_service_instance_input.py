"""Generated from Smithy shape ``com.amazonaws.proton#UpdateServiceInstanceInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.client_token
    import aws_sdk_proton.types.deployment_update_type
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.spec_contents
    import aws_sdk_proton.types.template_version_part


class UpdateServiceInstanceInput(TypedDict):
    name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the service instance to update.</p>"""
    service_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the service that the service instance belongs to.</p>"""
    deployment_type: "aws_sdk_proton.types.deployment_update_type.DeploymentUpdateType"
    """<p>The deployment type. It defines the mode for updating a service instance, as follows:</p> <dl> <dt/> <dd> <p> <code>NONE</code> </p> <p>In this mode, a deployment <i>doesn't</i> occur. Only the requested metadata parameters are updated.</p> </dd> <dt/> <dd> <p> <code>CURRENT_VERSION</code> </p> <p>In this mode, the service instance is deployed and updated with the new spec that you provide. Only requested parameters are updated. <i>Don’t</i> include major or minor version parameters when you use this deployment type.</p> </dd> <dt/> <dd> <p> <code>MINOR_VERSION</code> </p> <p>In this mode, the service instance is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can also specify a different minor version of the current major version in use.</p> </dd> <dt/> <dd> <p> <code>MAJOR_VERSION</code> </p> <p>In this mode, the service instance is deployed and updated with the published, recommended (latest) major and minor version of the current template, by default. You can specify a different major version that's higher than the major version in use and a minor version.</p> </dd> </dl>"""
    spec: NotRequired["aws_sdk_proton.types.spec_contents.SpecContents"]
    """<p>The formatted specification that defines the service instance update.</p>"""
    template_major_version: NotRequired[
        "aws_sdk_proton.types.template_version_part.TemplateVersionPart"
    ]
    """<p>The major version of the service template to update.</p>"""
    template_minor_version: NotRequired[
        "aws_sdk_proton.types.template_version_part.TemplateVersionPart"
    ]
    """<p>The minor version of the service template to update.</p>"""
    client_token: NotRequired["aws_sdk_proton.types.client_token.ClientToken"]
    """<p>The client token of the service instance to update.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateServiceInstanceInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["serviceName"] = value["service_name"]
    out["deploymentType"] = value["deployment_type"]
    if "spec" in value:
        out["spec"] = value["spec"]
    if "template_major_version" in value:
        out["templateMajorVersion"] = value["template_major_version"]
    if "template_minor_version" in value:
        out["templateMinorVersion"] = value["template_minor_version"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateServiceInstanceInput:
    out: UpdateServiceInstanceInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateServiceInstanceInput.name required")
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    else:
        raise DeserializationError("UpdateServiceInstanceInput.service_name required")
    if "deploymentType" in data:
        out["deployment_type"] = data["deploymentType"]
    else:
        raise DeserializationError(
            "UpdateServiceInstanceInput.deployment_type required"
        )
    if "spec" in data:
        out["spec"] = data["spec"]
    if "templateMajorVersion" in data:
        out["template_major_version"] = data["templateMajorVersion"]
    if "templateMinorVersion" in data:
        out["template_minor_version"] = data["templateMinorVersion"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
