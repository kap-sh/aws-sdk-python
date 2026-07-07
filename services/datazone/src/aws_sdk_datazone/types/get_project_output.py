"""Generated from Smithy shape ``com.amazonaws.datazone#GetProjectOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_datazone.types.created_by
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.domain_unit_id
    import aws_sdk_datazone.types.environment_configuration_user_parameters_list
    import aws_sdk_datazone.types.environment_deployment_details
    import aws_sdk_datazone.types.failure_reasons
    import aws_sdk_datazone.types.glossary_terms
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.project_name
    import aws_sdk_datazone.types.project_profile_id
    import aws_sdk_datazone.types.project_status
    import aws_sdk_datazone.types.resource_tags


class GetProjectOutput(TypedDict, closed=True):
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the project exists.</p>"""
    id: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>&gt;The ID of the project.</p>"""
    name: "aws_sdk_datazone.types.project_name.ProjectName"
    """<p>The name of the project.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of the project.</p>"""
    project_status: NotRequired["aws_sdk_datazone.types.project_status.ProjectStatus"]
    """<p>The status of the project.</p>"""
    failure_reasons: NotRequired[
        "aws_sdk_datazone.types.failure_reasons.FailureReasons"
    ]
    """<p>Specifies the error message that is returned if the operation cannot be successfully completed.</p>"""
    created_by: "aws_sdk_datazone.types.created_by.CreatedBy"
    """<p>The Amazon DataZone user who created the project.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the project was created.</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the project was last updated.</p>"""
    resource_tags: NotRequired["aws_sdk_datazone.types.resource_tags.ResourceTags"]
    """<p>The resource tags of the project.</p>"""
    glossary_terms: NotRequired["aws_sdk_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The business glossary terms that can be used in the project.</p>"""
    domain_unit_id: NotRequired["aws_sdk_datazone.types.domain_unit_id.DomainUnitId"]
    """<p>The ID of the domain unit.</p>"""
    project_profile_id: NotRequired[
        "aws_sdk_datazone.types.project_profile_id.ProjectProfileId"
    ]
    """<p>The ID of the project profile of a project.</p>"""
    user_parameters: NotRequired[
        "aws_sdk_datazone.types.environment_configuration_user_parameters_list.EnvironmentConfigurationUserParametersList"
    ]
    """<p>The user parameters of a project.</p>"""
    environment_deployment_details: NotRequired[
        "aws_sdk_datazone.types.environment_deployment_details.EnvironmentDeploymentDetails"
    ]
    """<p>The environment deployment status of a project.</p>"""
    project_category: NotRequired["str"]
    """<p>The category of the project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProjectOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "project_status" in value:
        import aws_sdk_datazone.types.project_status

        out["projectStatus"] = aws_sdk_datazone.types.project_status.serialize_json(
            value["project_status"]
        )
    if "failure_reasons" in value:
        import aws_sdk_datazone.types.failure_reasons

        out["failureReasons"] = aws_sdk_datazone.types.failure_reasons.serialize_json(
            value["failure_reasons"]
        )
    out["createdBy"] = value["created_by"]
    if "created_at" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["createdAt"] = aws_sdk_datazone.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["lastUpdatedAt"] = aws_sdk_datazone.types._prelude.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "resource_tags" in value:
        import aws_sdk_datazone.types.resource_tags

        out["resourceTags"] = aws_sdk_datazone.types.resource_tags.serialize_json(
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
    if "environment_deployment_details" in value:
        import aws_sdk_datazone.types.environment_deployment_details

        out["environmentDeploymentDetails"] = (
            aws_sdk_datazone.types.environment_deployment_details.serialize_json(
                value["environment_deployment_details"]
            )
        )
    if "project_category" in value:
        out["projectCategory"] = value["project_category"]
    return out


def deserialize_json(data: dict) -> GetProjectOutput:
    out: GetProjectOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("GetProjectOutput.domain_id required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetProjectOutput.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetProjectOutput.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "projectStatus" in data:
        import aws_sdk_datazone.types.project_status

        out["project_status"] = aws_sdk_datazone.types.project_status.deserialize_json(
            data["projectStatus"]
        )
    if "failureReasons" in data:
        import aws_sdk_datazone.types.failure_reasons

        out["failure_reasons"] = (
            aws_sdk_datazone.types.failure_reasons.deserialize_json(
                data["failureReasons"]
            )
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("GetProjectOutput.created_by required")
    if "createdAt" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["created_at"] = aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["last_updated_at"] = (
            aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    if "resourceTags" in data:
        import aws_sdk_datazone.types.resource_tags

        out["resource_tags"] = aws_sdk_datazone.types.resource_tags.deserialize_json(
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
    if "environmentDeploymentDetails" in data:
        import aws_sdk_datazone.types.environment_deployment_details

        out["environment_deployment_details"] = (
            aws_sdk_datazone.types.environment_deployment_details.deserialize_json(
                data["environmentDeploymentDetails"]
            )
        )
    if "projectCategory" in data:
        out["project_category"] = data["projectCategory"]
    return out
