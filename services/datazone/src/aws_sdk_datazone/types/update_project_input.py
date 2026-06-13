"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateProjectInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.domain_unit_id
    import aws_sdk_datazone.types.environment_configuration_user_parameters_list
    import aws_sdk_datazone.types.environment_deployment_details
    import aws_sdk_datazone.types.glossary_terms
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.project_name
    import aws_sdk_datazone.types.tags


class UpdateProjectInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain where a project is being updated.</p>"""
    identifier: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project that is to be updated.</p>"""
    name: NotRequired["aws_sdk_datazone.types.project_name.ProjectName"]
    """<p>The name to be updated as part of the <code>UpdateProject</code> action.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description to be updated as part of the <code>UpdateProject</code> action.</p>"""
    resource_tags: NotRequired["aws_sdk_datazone.types.tags.Tags"]
    """<p>The resource tags of the project.</p>"""
    glossary_terms: NotRequired["aws_sdk_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The glossary terms to be updated as part of the <code>UpdateProject</code> action.</p>"""
    domain_unit_id: NotRequired["aws_sdk_datazone.types.domain_unit_id.DomainUnitId"]
    """<p>The ID of the domain unit.</p>"""
    environment_deployment_details: NotRequired[
        "aws_sdk_datazone.types.environment_deployment_details.EnvironmentDeploymentDetails"
    ]
    """<p>The environment deployment details of the project.</p>"""
    user_parameters: NotRequired[
        "aws_sdk_datazone.types.environment_configuration_user_parameters_list.EnvironmentConfigurationUserParametersList"
    ]
    """<p>The user parameters of the project.</p>"""
    project_profile_version: NotRequired["str"]
    """<p>The project profile version to which the project should be updated. You can only specify the following string for this parameter: <code>latest</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProjectInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "resource_tags" in value:
        import aws_sdk_datazone.types.tags

        out["resourceTags"] = aws_sdk_datazone.types.tags.serialize_json(
            value["resource_tags"]
        )
    if "glossary_terms" in value:
        import aws_sdk_datazone.types.glossary_terms

        out["glossaryTerms"] = aws_sdk_datazone.types.glossary_terms.serialize_json(
            value["glossary_terms"]
        )
    if "domain_unit_id" in value:
        out["domainUnitId"] = value["domain_unit_id"]
    if "environment_deployment_details" in value:
        import aws_sdk_datazone.types.environment_deployment_details

        out["environmentDeploymentDetails"] = (
            aws_sdk_datazone.types.environment_deployment_details.serialize_json(
                value["environment_deployment_details"]
            )
        )
    if "user_parameters" in value:
        import aws_sdk_datazone.types.environment_configuration_user_parameters_list

        out["userParameters"] = (
            aws_sdk_datazone.types.environment_configuration_user_parameters_list.serialize_json(
                value["user_parameters"]
            )
        )
    if "project_profile_version" in value:
        out["projectProfileVersion"] = value["project_profile_version"]
    return out


def deserialize_json(data: dict) -> UpdateProjectInput:
    out: UpdateProjectInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "resourceTags" in data:
        import aws_sdk_datazone.types.tags

        out["resource_tags"] = aws_sdk_datazone.types.tags.deserialize_json(
            data["resourceTags"]
        )
    if "glossaryTerms" in data:
        import aws_sdk_datazone.types.glossary_terms

        out["glossary_terms"] = aws_sdk_datazone.types.glossary_terms.deserialize_json(
            data["glossaryTerms"]
        )
    if "domainUnitId" in data:
        out["domain_unit_id"] = data["domainUnitId"]
    if "environmentDeploymentDetails" in data:
        import aws_sdk_datazone.types.environment_deployment_details

        out["environment_deployment_details"] = (
            aws_sdk_datazone.types.environment_deployment_details.deserialize_json(
                data["environmentDeploymentDetails"]
            )
        )
    if "userParameters" in data:
        import aws_sdk_datazone.types.environment_configuration_user_parameters_list

        out["user_parameters"] = (
            aws_sdk_datazone.types.environment_configuration_user_parameters_list.deserialize_json(
                data["userParameters"]
            )
        )
    if "projectProfileVersion" in data:
        out["project_profile_version"] = data["projectProfileVersion"]
    return out
