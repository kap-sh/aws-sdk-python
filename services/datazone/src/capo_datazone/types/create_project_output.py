"""Generated from Smithy shape ``com.amazonaws.datazone#CreateProjectOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.created_by
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.domain_unit_id
    import capo_datazone.types.environment_configuration_user_parameters_list
    import capo_datazone.types.environment_deployment_details
    import capo_datazone.types.failure_reasons
    import capo_datazone.types.glossary_terms
    import capo_datazone.types.project_id
    import capo_datazone.types.project_name
    import capo_datazone.types.project_profile_id
    import capo_datazone.types.project_status
    import capo_datazone.types.resource_tags


class CreateProjectOutput(TypedDict, closed=True):
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which the project was created.</p>"""
    id: "capo_datazone.types.project_id.ProjectId"
    """<p>The ID of the Amazon DataZone project.</p>"""
    name: "capo_datazone.types.project_name.ProjectName"
    """<p>The name of the project.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of the project.</p>"""
    project_status: NotRequired["capo_datazone.types.project_status.ProjectStatus"]
    """<p>The status of the Amazon DataZone project that was created.</p>"""
    failure_reasons: NotRequired["capo_datazone.types.failure_reasons.FailureReasons"]
    """<p>Specifies the error message that is returned if the operation cannot be successfully completed.</p>"""
    created_by: "capo_datazone.types.created_by.CreatedBy"
    """<p>The Amazon DataZone user who created the project.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the project was created.</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the project was last updated.</p>"""
    resource_tags: NotRequired["capo_datazone.types.resource_tags.ResourceTags"]
    """<p>The resource tags of the project.</p>"""
    glossary_terms: NotRequired["capo_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The glossary terms that can be used in the project.</p>"""
    domain_unit_id: NotRequired["capo_datazone.types.domain_unit_id.DomainUnitId"]
    """<p>The ID of the domain unit.</p>"""
    project_profile_id: NotRequired[
        "capo_datazone.types.project_profile_id.ProjectProfileId"
    ]
    """<p>The project profile ID.</p>"""
    user_parameters: NotRequired[
        "capo_datazone.types.environment_configuration_user_parameters_list.EnvironmentConfigurationUserParametersList"
    ]
    """<p>The user parameters of the project.</p>"""
    environment_deployment_details: NotRequired[
        "capo_datazone.types.environment_deployment_details.EnvironmentDeploymentDetails"
    ]
    """<p>The environment deployment details.</p>"""
    project_category: NotRequired["str"]
    """<p>The category of the project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProjectOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "project_status" in value:
        import capo_datazone.types.project_status

        out["projectStatus"] = capo_datazone.types.project_status.serialize_json(
            value["project_status"]
        )
    if "failure_reasons" in value:
        import capo_datazone.types.failure_reasons

        out["failureReasons"] = capo_datazone.types.failure_reasons.serialize_json(
            value["failure_reasons"]
        )
    out["createdBy"] = value["created_by"]
    if "created_at" in value:
        import capo_datazone.types._prelude.timestamp

        out["createdAt"] = capo_datazone.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_datazone.types._prelude.timestamp

        out["lastUpdatedAt"] = capo_datazone.types._prelude.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "resource_tags" in value:
        import capo_datazone.types.resource_tags

        out["resourceTags"] = capo_datazone.types.resource_tags.serialize_json(
            value["resource_tags"]
        )
    if "glossary_terms" in value:
        import capo_datazone.types.glossary_terms

        out["glossaryTerms"] = capo_datazone.types.glossary_terms.serialize_json(
            value["glossary_terms"]
        )
    if "domain_unit_id" in value:
        out["domainUnitId"] = value["domain_unit_id"]
    if "project_profile_id" in value:
        out["projectProfileId"] = value["project_profile_id"]
    if "user_parameters" in value:
        import capo_datazone.types.environment_configuration_user_parameters_list

        out["userParameters"] = (
            capo_datazone.types.environment_configuration_user_parameters_list.serialize_json(
                value["user_parameters"]
            )
        )
    if "environment_deployment_details" in value:
        import capo_datazone.types.environment_deployment_details

        out["environmentDeploymentDetails"] = (
            capo_datazone.types.environment_deployment_details.serialize_json(
                value["environment_deployment_details"]
            )
        )
    if "project_category" in value:
        out["projectCategory"] = value["project_category"]
    return out


def deserialize_json(data: dict) -> CreateProjectOutput:
    out: CreateProjectOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("CreateProjectOutput.domain_id required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateProjectOutput.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateProjectOutput.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "projectStatus" in data:
        import capo_datazone.types.project_status

        out["project_status"] = capo_datazone.types.project_status.deserialize_json(
            data["projectStatus"]
        )
    if "failureReasons" in data:
        import capo_datazone.types.failure_reasons

        out["failure_reasons"] = capo_datazone.types.failure_reasons.deserialize_json(
            data["failureReasons"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("CreateProjectOutput.created_by required")
    if "createdAt" in data:
        import capo_datazone.types._prelude.timestamp

        out["created_at"] = capo_datazone.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "lastUpdatedAt" in data:
        import capo_datazone.types._prelude.timestamp

        out["last_updated_at"] = (
            capo_datazone.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    if "resourceTags" in data:
        import capo_datazone.types.resource_tags

        out["resource_tags"] = capo_datazone.types.resource_tags.deserialize_json(
            data["resourceTags"]
        )
    if "glossaryTerms" in data:
        import capo_datazone.types.glossary_terms

        out["glossary_terms"] = capo_datazone.types.glossary_terms.deserialize_json(
            data["glossaryTerms"]
        )
    if "domainUnitId" in data:
        out["domain_unit_id"] = data["domainUnitId"]
    if "projectProfileId" in data:
        out["project_profile_id"] = data["projectProfileId"]
    if "userParameters" in data:
        import capo_datazone.types.environment_configuration_user_parameters_list

        out["user_parameters"] = (
            capo_datazone.types.environment_configuration_user_parameters_list.deserialize_json(
                data["userParameters"]
            )
        )
    if "environmentDeploymentDetails" in data:
        import capo_datazone.types.environment_deployment_details

        out["environment_deployment_details"] = (
            capo_datazone.types.environment_deployment_details.deserialize_json(
                data["environmentDeploymentDetails"]
            )
        )
    if "projectCategory" in data:
        out["project_category"] = data["projectCategory"]
    return out
