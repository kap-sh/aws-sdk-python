"""Generated from Smithy shape ``com.amazonaws.datazone#CreateEnvironmentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_configuration_name
    import aws_sdk_datazone.types.environment_parameters_list
    import aws_sdk_datazone.types.environment_profile_id
    import aws_sdk_datazone.types.glossary_terms
    import aws_sdk_datazone.types.project_id


class CreateEnvironmentInput(TypedDict, closed=True):
    project_identifier: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The identifier of the Amazon DataZone project in which this environment is created.</p>"""
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which the environment is created.</p>"""
    description: NotRequired["str"]
    """<p>The description of the Amazon DataZone environment.</p>"""
    name: "str"
    """<p>The name of the Amazon DataZone environment.</p>"""
    environment_profile_identifier: NotRequired[
        "aws_sdk_datazone.types.environment_profile_id.EnvironmentProfileId"
    ]
    """<p>The identifier of the environment profile that is used to create this Amazon DataZone environment.</p>"""
    user_parameters: NotRequired[
        "aws_sdk_datazone.types.environment_parameters_list.EnvironmentParametersList"
    ]
    """<p>The user parameters of this Amazon DataZone environment.</p>"""
    glossary_terms: NotRequired["aws_sdk_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The glossary terms that can be used in this Amazon DataZone environment.</p>"""
    environment_account_identifier: NotRequired["str"]
    """<p>The ID of the account in which the environment is being created.</p>"""
    environment_account_region: NotRequired["str"]
    """<p>The region of the account in which the environment is being created.</p>"""
    environment_blueprint_identifier: NotRequired["str"]
    """<p>The ID of the blueprint with which the environment is being created.</p>"""
    deployment_order: NotRequired["int"]
    """<p>The deployment order of the environment.</p>"""
    environment_configuration_id: NotRequired["str"]
    """<p>The configuration ID of the environment.</p>"""
    environment_configuration_name: NotRequired[
        "aws_sdk_datazone.types.environment_configuration_name.EnvironmentConfigurationName"
    ]
    """<p>The configuration name of the environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEnvironmentInput) -> dict:
    out: dict = {}
    out["projectIdentifier"] = value["project_identifier"]
    if "description" in value:
        out["description"] = value["description"]
    out["name"] = value["name"]
    if "environment_profile_identifier" in value:
        out["environmentProfileIdentifier"] = value["environment_profile_identifier"]
    if "user_parameters" in value:
        import aws_sdk_datazone.types.environment_parameters_list

        out["userParameters"] = (
            aws_sdk_datazone.types.environment_parameters_list.serialize_json(
                value["user_parameters"]
            )
        )
    if "glossary_terms" in value:
        import aws_sdk_datazone.types.glossary_terms

        out["glossaryTerms"] = aws_sdk_datazone.types.glossary_terms.serialize_json(
            value["glossary_terms"]
        )
    if "environment_account_identifier" in value:
        out["environmentAccountIdentifier"] = value["environment_account_identifier"]
    if "environment_account_region" in value:
        out["environmentAccountRegion"] = value["environment_account_region"]
    if "environment_blueprint_identifier" in value:
        out["environmentBlueprintIdentifier"] = value[
            "environment_blueprint_identifier"
        ]
    if "deployment_order" in value:
        out["deploymentOrder"] = value["deployment_order"]
    if "environment_configuration_id" in value:
        out["environmentConfigurationId"] = value["environment_configuration_id"]
    if "environment_configuration_name" in value:
        out["environmentConfigurationName"] = value["environment_configuration_name"]
    return out


def deserialize_json(data: dict) -> CreateEnvironmentInput:
    out: CreateEnvironmentInput = {}  # type: ignore[typeddict-item]
    if "projectIdentifier" in data:
        out["project_identifier"] = data["projectIdentifier"]
    else:
        raise DeserializationError("CreateEnvironmentInput.project_identifier required")
    if "description" in data:
        out["description"] = data["description"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateEnvironmentInput.name required")
    if "environmentProfileIdentifier" in data:
        out["environment_profile_identifier"] = data["environmentProfileIdentifier"]
    if "userParameters" in data:
        import aws_sdk_datazone.types.environment_parameters_list

        out["user_parameters"] = (
            aws_sdk_datazone.types.environment_parameters_list.deserialize_json(
                data["userParameters"]
            )
        )
    if "glossaryTerms" in data:
        import aws_sdk_datazone.types.glossary_terms

        out["glossary_terms"] = aws_sdk_datazone.types.glossary_terms.deserialize_json(
            data["glossaryTerms"]
        )
    if "environmentAccountIdentifier" in data:
        out["environment_account_identifier"] = data["environmentAccountIdentifier"]
    if "environmentAccountRegion" in data:
        out["environment_account_region"] = data["environmentAccountRegion"]
    if "environmentBlueprintIdentifier" in data:
        out["environment_blueprint_identifier"] = data["environmentBlueprintIdentifier"]
    if "deploymentOrder" in data:
        out["deployment_order"] = data["deploymentOrder"]
    if "environmentConfigurationId" in data:
        out["environment_configuration_id"] = data["environmentConfigurationId"]
    if "environmentConfigurationName" in data:
        out["environment_configuration_name"] = data["environmentConfigurationName"]
    return out
