"""Generated from Smithy shape ``com.amazonaws.proton#ServicePipelineState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.spec_contents
    import aws_sdk_proton.types.template_version_part


class ServicePipelineState(TypedDict):
    spec: NotRequired["aws_sdk_proton.types.spec_contents.SpecContents"]
    """<p>The service spec that was used to create the service pipeline.</p>"""
    template_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the service template that was used to create the service pipeline.</p>"""
    template_major_version: (
        "aws_sdk_proton.types.template_version_part.TemplateVersionPart"
    )
    """<p>The major version of the service template that was used to create the service pipeline.</p>"""
    template_minor_version: (
        "aws_sdk_proton.types.template_version_part.TemplateVersionPart"
    )
    """<p>The minor version of the service template that was used to create the service pipeline.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServicePipelineState) -> dict:
    out: dict = {}
    if "spec" in value:
        out["spec"] = value["spec"]
    out["templateName"] = value["template_name"]
    out["templateMajorVersion"] = value["template_major_version"]
    out["templateMinorVersion"] = value["template_minor_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ServicePipelineState:
    out: ServicePipelineState = {}  # type: ignore[typeddict-item]
    if "spec" in data:
        out["spec"] = data["spec"]
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError("ServicePipelineState.template_name required")
    if "templateMajorVersion" in data:
        out["template_major_version"] = data["templateMajorVersion"]
    else:
        raise DeserializationError(
            "ServicePipelineState.template_major_version required"
        )
    if "templateMinorVersion" in data:
        out["template_minor_version"] = data["templateMinorVersion"]
    else:
        raise DeserializationError(
            "ServicePipelineState.template_minor_version required"
        )
    return out
