"""Generated from Smithy shape ``com.amazonaws.datazone#CreateProjectInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.domain_unit_id
    import aws_sdk_datazone.types.environment_configuration_user_parameters_list
    import aws_sdk_datazone.types.glossary_terms
    import aws_sdk_datazone.types.project_membership_assignments
    import aws_sdk_datazone.types.project_name
    import aws_sdk_datazone.types.project_profile_id
    import aws_sdk_datazone.types.role_arn
    import aws_sdk_datazone.types.tags


class CreateProjectInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which this project is created.</p>"""
    name: "aws_sdk_datazone.types.project_name.ProjectName"
    """<p>The name of the Amazon DataZone project.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of the Amazon DataZone project.</p>"""
    resource_tags: NotRequired["aws_sdk_datazone.types.tags.Tags"]
    """<p>The resource tags of the project.</p>"""
    glossary_terms: NotRequired["aws_sdk_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The glossary terms that can be used in this Amazon DataZone project.</p>"""
    domain_unit_id: NotRequired["aws_sdk_datazone.types.domain_unit_id.DomainUnitId"]
    """<p>The ID of the domain unit. This parameter is not required and if it is not specified, then the project is created at the root domain unit level.</p>"""
    project_profile_id: NotRequired[
        "aws_sdk_datazone.types.project_profile_id.ProjectProfileId"
    ]
    """<p>The ID of the project profile.</p>"""
    user_parameters: NotRequired[
        "aws_sdk_datazone.types.environment_configuration_user_parameters_list.EnvironmentConfigurationUserParametersList"
    ]
    """<p>The user parameters of the project.</p>"""
    project_category: NotRequired["str"]
    """<p>The category of the project. Set to 'ADMIN' designates this as an administrative project for the Amazon DataZone domain.</p>"""
    project_execution_role: NotRequired["aws_sdk_datazone.types.role_arn.RoleArn"]
    """<p>The default project IAM role that is used to access project resources and run computes such as Glue and Sagemaker.</p>"""
    membership_assignments: NotRequired[
        "aws_sdk_datazone.types.project_membership_assignments.ProjectMembershipAssignments"
    ]
    """<p>The members to be assigned to the project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProjectInput) -> dict:
    out: dict = {}
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
    if "project_profile_id" in value:
        out["projectProfileId"] = value["project_profile_id"]
    if "user_parameters" in value:
        import aws_sdk_datazone.types.environment_configuration_user_parameters_list

        out["userParameters"] = (
            aws_sdk_datazone.types.environment_configuration_user_parameters_list.serialize_json(
                value["user_parameters"]
            )
        )
    if "project_category" in value:
        out["projectCategory"] = value["project_category"]
    if "project_execution_role" in value:
        out["projectExecutionRole"] = value["project_execution_role"]
    if "membership_assignments" in value:
        import aws_sdk_datazone.types.project_membership_assignments

        out["membershipAssignments"] = (
            aws_sdk_datazone.types.project_membership_assignments.serialize_json(
                value["membership_assignments"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateProjectInput:
    out: CreateProjectInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateProjectInput.name required")
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
    if "projectProfileId" in data:
        out["project_profile_id"] = data["projectProfileId"]
    if "userParameters" in data:
        import aws_sdk_datazone.types.environment_configuration_user_parameters_list

        out["user_parameters"] = (
            aws_sdk_datazone.types.environment_configuration_user_parameters_list.deserialize_json(
                data["userParameters"]
            )
        )
    if "projectCategory" in data:
        out["project_category"] = data["projectCategory"]
    if "projectExecutionRole" in data:
        out["project_execution_role"] = data["projectExecutionRole"]
    if "membershipAssignments" in data:
        import aws_sdk_datazone.types.project_membership_assignments

        out["membership_assignments"] = (
            aws_sdk_datazone.types.project_membership_assignments.deserialize_json(
                data["membershipAssignments"]
            )
        )
    return out
