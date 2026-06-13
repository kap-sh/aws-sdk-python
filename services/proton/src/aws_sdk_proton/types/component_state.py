"""Generated from Smithy shape ``com.amazonaws.proton#ComponentState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_proton.types.resource_name_or_empty
    import aws_sdk_proton.types.spec_contents
    import aws_sdk_proton.types.template_file_contents


class ComponentState(TypedDict):
    service_name: NotRequired[
        "aws_sdk_proton.types.resource_name_or_empty.ResourceNameOrEmpty"
    ]
    """<p>The name of the service that <code>serviceInstanceName</code> is associated with. Provided when a component is attached to a service instance.</p>"""
    service_instance_name: NotRequired[
        "aws_sdk_proton.types.resource_name_or_empty.ResourceNameOrEmpty"
    ]
    """<p>The name of the service instance that this component is attached to. Provided when a component is attached to a service instance.</p>"""
    service_spec: NotRequired["aws_sdk_proton.types.spec_contents.SpecContents"]
    """<p>The service spec that the component uses to access service inputs. Provided when a component is attached to a service instance.</p>"""
    template_file: NotRequired[
        "aws_sdk_proton.types.template_file_contents.TemplateFileContents"
    ]
    """<p>The template file used.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ComponentState) -> dict:
    out: dict = {}
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "service_instance_name" in value:
        out["serviceInstanceName"] = value["service_instance_name"]
    if "service_spec" in value:
        out["serviceSpec"] = value["service_spec"]
    if "template_file" in value:
        out["templateFile"] = value["template_file"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ComponentState:
    out: ComponentState = {}  # type: ignore[typeddict-item]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    if "serviceInstanceName" in data:
        out["service_instance_name"] = data["serviceInstanceName"]
    if "serviceSpec" in data:
        out["service_spec"] = data["serviceSpec"]
    if "templateFile" in data:
        out["template_file"] = data["templateFile"]
    return out
