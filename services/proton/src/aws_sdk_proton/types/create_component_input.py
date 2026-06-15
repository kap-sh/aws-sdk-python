"""Generated from Smithy shape ``com.amazonaws.proton#CreateComponentInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.client_token
    import aws_sdk_proton.types.description
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.spec_contents
    import aws_sdk_proton.types.tag_list
    import aws_sdk_proton.types.template_file_contents
    import aws_sdk_proton.types.template_manifest_contents


class CreateComponentInput(TypedDict):
    name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The customer-provided name of the component.</p>"""
    description: NotRequired["aws_sdk_proton.types.description.Description"]
    """<p>An optional customer-provided description of the component.</p>"""
    service_name: NotRequired["aws_sdk_proton.types.resource_name.ResourceName"]
    """<p>The name of the service that <code>serviceInstanceName</code> is associated with. If you don't specify this, the component isn't attached to any service instance. Specify both <code>serviceInstanceName</code> and <code>serviceName</code> or neither of them.</p>"""
    service_instance_name: NotRequired[
        "aws_sdk_proton.types.resource_name.ResourceName"
    ]
    """<p>The name of the service instance that you want to attach this component to. If you don't specify this, the component isn't attached to any service instance. Specify both <code>serviceInstanceName</code> and <code>serviceName</code> or neither of them.</p>"""
    environment_name: NotRequired["aws_sdk_proton.types.resource_name.ResourceName"]
    """<p>The name of the Proton environment that you want to associate this component with. You must specify this when you don't specify <code>serviceInstanceName</code> and <code>serviceName</code>.</p>"""
    template_file: "aws_sdk_proton.types.template_file_contents.TemplateFileContents"
    """<p>A path to the Infrastructure as Code (IaC) file describing infrastructure that a custom component provisions.</p> <note> <p>Components support a single IaC file, even if you use Terraform as your template language.</p> </note>"""
    manifest: "aws_sdk_proton.types.template_manifest_contents.TemplateManifestContents"
    """<p>A path to a manifest file that lists the Infrastructure as Code (IaC) file, template language, and rendering engine for infrastructure that a custom component provisions.</p>"""
    service_spec: NotRequired["aws_sdk_proton.types.spec_contents.SpecContents"]
    """<p>The service spec that you want the component to use to access service inputs. Set this only when you attach the component to a service instance.</p>"""
    tags: NotRequired["aws_sdk_proton.types.tag_list.TagList"]
    r"""<p>An optional list of metadata items that you can associate with the Proton component. A tag is a key-value pair.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/resources.html\">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>"""
    client_token: NotRequired["aws_sdk_proton.types.client_token.ClientToken"]
    """<p>The client token for the created component.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateComponentInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "service_instance_name" in value:
        out["serviceInstanceName"] = value["service_instance_name"]
    if "environment_name" in value:
        out["environmentName"] = value["environment_name"]
    out["templateFile"] = value["template_file"]
    out["manifest"] = value["manifest"]
    if "service_spec" in value:
        out["serviceSpec"] = value["service_spec"]
    if "tags" in value:
        import aws_sdk_proton.types.tag_list

        out["tags"] = aws_sdk_proton.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateComponentInput:
    out: CreateComponentInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateComponentInput.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    if "serviceInstanceName" in data:
        out["service_instance_name"] = data["serviceInstanceName"]
    if "environmentName" in data:
        out["environment_name"] = data["environmentName"]
    if "templateFile" in data:
        out["template_file"] = data["templateFile"]
    else:
        raise DeserializationError("CreateComponentInput.template_file required")
    if "manifest" in data:
        out["manifest"] = data["manifest"]
    else:
        raise DeserializationError("CreateComponentInput.manifest required")
    if "serviceSpec" in data:
        out["service_spec"] = data["serviceSpec"]
    if "tags" in data:
        import aws_sdk_proton.types.tag_list

        out["tags"] = aws_sdk_proton.types.tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
