"""Generated from Smithy shape ``com.amazonaws.proton#ServiceInstanceState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.component_deployment_id_list
    import aws_sdk_proton.types.deployment_id
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.spec_contents
    import aws_sdk_proton.types.template_version_part


class ServiceInstanceState(TypedDict, closed=True):
    spec: "aws_sdk_proton.types.spec_contents.SpecContents"
    """<p>The service spec that was used to create the service instance.</p>"""
    template_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the service template that was used to create the service instance.</p>"""
    template_major_version: (
        "aws_sdk_proton.types.template_version_part.TemplateVersionPart"
    )
    """<p>The major version of the service template that was used to create the service pipeline.</p>"""
    template_minor_version: (
        "aws_sdk_proton.types.template_version_part.TemplateVersionPart"
    )
    """<p>The minor version of the service template that was used to create the service pipeline.</p>"""
    last_successful_component_deployment_ids: NotRequired[
        "aws_sdk_proton.types.component_deployment_id_list.ComponentDeploymentIdList"
    ]
    """<p>The IDs for the last successful components deployed for this service instance.</p>"""
    last_successful_environment_deployment_id: NotRequired[
        "aws_sdk_proton.types.deployment_id.DeploymentId"
    ]
    """<p>The ID for the last successful environment deployed for this service instance.</p>"""
    last_successful_service_pipeline_deployment_id: NotRequired[
        "aws_sdk_proton.types.deployment_id.DeploymentId"
    ]
    """<p>The ID for the last successful service pipeline deployed for this service instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceInstanceState) -> dict:
    out: dict = {}
    out["spec"] = value["spec"]
    out["templateName"] = value["template_name"]
    out["templateMajorVersion"] = value["template_major_version"]
    out["templateMinorVersion"] = value["template_minor_version"]
    if "last_successful_component_deployment_ids" in value:
        import aws_sdk_proton.types.component_deployment_id_list

        out["lastSuccessfulComponentDeploymentIds"] = (
            aws_sdk_proton.types.component_deployment_id_list.serialize_aws_json_1_0(
                value["last_successful_component_deployment_ids"]
            )
        )
    if "last_successful_environment_deployment_id" in value:
        out["lastSuccessfulEnvironmentDeploymentId"] = value[
            "last_successful_environment_deployment_id"
        ]
    if "last_successful_service_pipeline_deployment_id" in value:
        out["lastSuccessfulServicePipelineDeploymentId"] = value[
            "last_successful_service_pipeline_deployment_id"
        ]
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceInstanceState:
    out: ServiceInstanceState = {}  # type: ignore[typeddict-item]
    if "spec" in data:
        out["spec"] = data["spec"]
    else:
        raise DeserializationError("ServiceInstanceState.spec required")
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError("ServiceInstanceState.template_name required")
    if "templateMajorVersion" in data:
        out["template_major_version"] = data["templateMajorVersion"]
    else:
        raise DeserializationError(
            "ServiceInstanceState.template_major_version required"
        )
    if "templateMinorVersion" in data:
        out["template_minor_version"] = data["templateMinorVersion"]
    else:
        raise DeserializationError(
            "ServiceInstanceState.template_minor_version required"
        )
    if "lastSuccessfulComponentDeploymentIds" in data:
        import aws_sdk_proton.types.component_deployment_id_list

        out["last_successful_component_deployment_ids"] = (
            aws_sdk_proton.types.component_deployment_id_list.deserialize_aws_json_1_0(
                data["lastSuccessfulComponentDeploymentIds"]
            )
        )
    if "lastSuccessfulEnvironmentDeploymentId" in data:
        out["last_successful_environment_deployment_id"] = data[
            "lastSuccessfulEnvironmentDeploymentId"
        ]
    if "lastSuccessfulServicePipelineDeploymentId" in data:
        out["last_successful_service_pipeline_deployment_id"] = data[
            "lastSuccessfulServicePipelineDeploymentId"
        ]
    return out
