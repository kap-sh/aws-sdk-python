"""Generated from Smithy shape ``com.amazonaws.proton#UpdateComponentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.client_token
    import aws_sdk_proton.types.component_deployment_update_type
    import aws_sdk_proton.types.description
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.resource_name_or_empty
    import aws_sdk_proton.types.spec_contents
    import aws_sdk_proton.types.template_file_contents


class UpdateComponentInput(TypedDict, closed=True):
    name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the component to update.</p>"""
    deployment_type: "aws_sdk_proton.types.component_deployment_update_type.ComponentDeploymentUpdateType"
    """<p>The deployment type. It defines the mode for updating a component, as follows:</p> <dl> <dt/> <dd> <p> <code>NONE</code> </p> <p>In this mode, a deployment <i>doesn't</i> occur. Only the requested metadata parameters are updated. You can only specify <code>description</code> in this mode.</p> </dd> <dt/> <dd> <p> <code>CURRENT_VERSION</code> </p> <p>In this mode, the component is deployed and updated with the new <code>serviceSpec</code>, <code>templateSource</code>, and/or <code>type</code> that you provide. Only requested parameters are updated.</p> </dd> </dl>"""
    description: NotRequired["aws_sdk_proton.types.description.Description"]
    """<p>An optional customer-provided description of the component.</p>"""
    service_name: NotRequired[
        "aws_sdk_proton.types.resource_name_or_empty.ResourceNameOrEmpty"
    ]
    """<p>The name of the service that <code>serviceInstanceName</code> is associated with. Don't specify to keep the component's current service instance attachment. Specify an empty string to detach the component from the service instance it's attached to. Specify non-empty values for both <code>serviceInstanceName</code> and <code>serviceName</code> or for neither of them.</p>"""
    service_instance_name: NotRequired[
        "aws_sdk_proton.types.resource_name_or_empty.ResourceNameOrEmpty"
    ]
    """<p>The name of the service instance that you want to attach this component to. Don't specify to keep the component's current service instance attachment. Specify an empty string to detach the component from the service instance it's attached to. Specify non-empty values for both <code>serviceInstanceName</code> and <code>serviceName</code> or for neither of them.</p>"""
    service_spec: NotRequired["aws_sdk_proton.types.spec_contents.SpecContents"]
    """<p>The service spec that you want the component to use to access service inputs. Set this only when the component is attached to a service instance.</p>"""
    template_file: NotRequired[
        "aws_sdk_proton.types.template_file_contents.TemplateFileContents"
    ]
    """<p>A path to the Infrastructure as Code (IaC) file describing infrastructure that a custom component provisions.</p> <note> <p>Components support a single IaC file, even if you use Terraform as your template language.</p> </note>"""
    client_token: NotRequired["aws_sdk_proton.types.client_token.ClientToken"]
    """<p>The client token for the updated component.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateComponentInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["deploymentType"] = value["deployment_type"]
    if "description" in value:
        out["description"] = value["description"]
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "service_instance_name" in value:
        out["serviceInstanceName"] = value["service_instance_name"]
    if "service_spec" in value:
        out["serviceSpec"] = value["service_spec"]
    if "template_file" in value:
        out["templateFile"] = value["template_file"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateComponentInput:
    out: UpdateComponentInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateComponentInput.name required")
    if "deploymentType" in data:
        out["deployment_type"] = data["deploymentType"]
    else:
        raise DeserializationError("UpdateComponentInput.deployment_type required")
    if "description" in data:
        out["description"] = data["description"]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    if "serviceInstanceName" in data:
        out["service_instance_name"] = data["serviceInstanceName"]
    if "serviceSpec" in data:
        out["service_spec"] = data["serviceSpec"]
    if "templateFile" in data:
        out["template_file"] = data["templateFile"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
