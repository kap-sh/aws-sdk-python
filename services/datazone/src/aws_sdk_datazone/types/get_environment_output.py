"""Generated from Smithy shape ``com.amazonaws.datazone#GetEnvironmentOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_datazone.types.aws_account_id
    import aws_sdk_datazone.types.aws_region
    import aws_sdk_datazone.types.custom_parameter_list
    import aws_sdk_datazone.types.deployment
    import aws_sdk_datazone.types.deployment_properties
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_action_list
    import aws_sdk_datazone.types.environment_blueprint_id
    import aws_sdk_datazone.types.environment_configuration_id
    import aws_sdk_datazone.types.environment_configuration_name
    import aws_sdk_datazone.types.environment_id
    import aws_sdk_datazone.types.environment_name
    import aws_sdk_datazone.types.environment_profile_id
    import aws_sdk_datazone.types.environment_status
    import aws_sdk_datazone.types.glossary_terms
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.provisioning_properties
    import aws_sdk_datazone.types.resource_list


class GetEnvironmentOutput(TypedDict):
    project_id: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The ID of the Amazon DataZone project in which this environment is created.</p>"""
    id: NotRequired["aws_sdk_datazone.types.environment_id.EnvironmentId"]
    """<p>The ID of the environment.</p>"""
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain where the environment exists.</p>"""
    created_by: "str"
    """<p>The Amazon DataZone user who created the environment.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the environment was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when this environment was updated.</p>"""
    name: "aws_sdk_datazone.types.environment_name.EnvironmentName"
    """<p>The name of the environment.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of the environment.</p>"""
    environment_profile_id: (
        "aws_sdk_datazone.types.environment_profile_id.EnvironmentProfileId"
    )
    """<p>The ID of the environment profile with which the environment is created.</p>"""
    aws_account_id: NotRequired["aws_sdk_datazone.types.aws_account_id.AwsAccountId"]
    """<p>The ID of the Amazon Web Services account where the environment exists.</p>"""
    aws_account_region: NotRequired["aws_sdk_datazone.types.aws_region.AwsRegion"]
    """<p>The Amazon Web Services region where the environment exists.</p>"""
    provider: "str"
    """<p>The provider of this Amazon DataZone environment.</p>"""
    provisioned_resources: NotRequired[
        "aws_sdk_datazone.types.resource_list.ResourceList"
    ]
    """<p>The provisioned resources of this Amazon DataZone environment.</p>"""
    status: NotRequired["aws_sdk_datazone.types.environment_status.EnvironmentStatus"]
    """<p>The status of this Amazon DataZone environment.</p>"""
    environment_actions: NotRequired[
        "aws_sdk_datazone.types.environment_action_list.EnvironmentActionList"
    ]
    """<p>The actions of the environment.</p>"""
    glossary_terms: NotRequired["aws_sdk_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The business glossary terms that can be used in this environment.</p>"""
    user_parameters: NotRequired[
        "aws_sdk_datazone.types.custom_parameter_list.CustomParameterList"
    ]
    """<p>The user parameters of this Amazon DataZone environment.</p>"""
    last_deployment: NotRequired["aws_sdk_datazone.types.deployment.Deployment"]
    """<p>The details of the last deployment of the environment.</p>"""
    provisioning_properties: NotRequired[
        "aws_sdk_datazone.types.provisioning_properties.ProvisioningProperties"
    ]
    """<p>The provisioning properties of this Amazon DataZone environment.</p>"""
    deployment_properties: NotRequired[
        "aws_sdk_datazone.types.deployment_properties.DeploymentProperties"
    ]
    """<p>The deployment properties of the environment.</p>"""
    environment_blueprint_id: NotRequired[
        "aws_sdk_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
    ]
    """<p>The blueprint with which the environment is created.</p>"""
    environment_configuration_id: NotRequired[
        "aws_sdk_datazone.types.environment_configuration_id.EnvironmentConfigurationId"
    ]
    """<p>The configuration ID that is used to create the environment.</p>"""
    environment_configuration_name: NotRequired[
        "aws_sdk_datazone.types.environment_configuration_name.EnvironmentConfigurationName"
    ]
    """<p>The configuration name that is used to create the environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnvironmentOutput) -> dict:
    out: dict = {}
    out["projectId"] = value["project_id"]
    if "id" in value:
        out["id"] = value["id"]
    out["domainId"] = value["domain_id"]
    out["createdBy"] = value["created_by"]
    if "created_at" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["createdAt"] = aws_sdk_datazone.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["updatedAt"] = aws_sdk_datazone.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["environmentProfileId"] = value.get("environment_profile_id", "")
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    if "aws_account_region" in value:
        out["awsAccountRegion"] = value["aws_account_region"]
    out["provider"] = value["provider"]
    if "provisioned_resources" in value:
        import aws_sdk_datazone.types.resource_list

        out["provisionedResources"] = (
            aws_sdk_datazone.types.resource_list.serialize_json(
                value["provisioned_resources"]
            )
        )
    if "status" in value:
        import aws_sdk_datazone.types.environment_status

        out["status"] = aws_sdk_datazone.types.environment_status.serialize_json(
            value["status"]
        )
    if "environment_actions" in value:
        import aws_sdk_datazone.types.environment_action_list

        out["environmentActions"] = (
            aws_sdk_datazone.types.environment_action_list.serialize_json(
                value["environment_actions"]
            )
        )
    if "glossary_terms" in value:
        import aws_sdk_datazone.types.glossary_terms

        out["glossaryTerms"] = aws_sdk_datazone.types.glossary_terms.serialize_json(
            value["glossary_terms"]
        )
    if "user_parameters" in value:
        import aws_sdk_datazone.types.custom_parameter_list

        out["userParameters"] = (
            aws_sdk_datazone.types.custom_parameter_list.serialize_json(
                value["user_parameters"]
            )
        )
    if "last_deployment" in value:
        import aws_sdk_datazone.types.deployment

        out["lastDeployment"] = aws_sdk_datazone.types.deployment.serialize_json(
            value["last_deployment"]
        )
    if "provisioning_properties" in value:
        import aws_sdk_datazone.types.provisioning_properties

        out["provisioningProperties"] = (
            aws_sdk_datazone.types.provisioning_properties.serialize_json(
                value["provisioning_properties"]
            )
        )
    if "deployment_properties" in value:
        import aws_sdk_datazone.types.deployment_properties

        out["deploymentProperties"] = (
            aws_sdk_datazone.types.deployment_properties.serialize_json(
                value["deployment_properties"]
            )
        )
    if "environment_blueprint_id" in value:
        out["environmentBlueprintId"] = value["environment_blueprint_id"]
    if "environment_configuration_id" in value:
        out["environmentConfigurationId"] = value["environment_configuration_id"]
    if "environment_configuration_name" in value:
        out["environmentConfigurationName"] = value["environment_configuration_name"]
    return out


def deserialize_json(data: dict) -> GetEnvironmentOutput:
    out: GetEnvironmentOutput = {}  # type: ignore[typeddict-item]
    if "projectId" in data:
        out["project_id"] = data["projectId"]
    else:
        raise DeserializationError("GetEnvironmentOutput.project_id required")
    if "id" in data:
        out["id"] = data["id"]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("GetEnvironmentOutput.domain_id required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("GetEnvironmentOutput.created_by required")
    if "createdAt" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["created_at"] = aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["updated_at"] = aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetEnvironmentOutput.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "environmentProfileId" in data:
        out["environment_profile_id"] = data["environmentProfileId"]
    else:
        out["environment_profile_id"] = ""
    if "awsAccountId" in data:
        out["aws_account_id"] = data["awsAccountId"]
    if "awsAccountRegion" in data:
        out["aws_account_region"] = data["awsAccountRegion"]
    if "provider" in data:
        out["provider"] = data["provider"]
    else:
        raise DeserializationError("GetEnvironmentOutput.provider required")
    if "provisionedResources" in data:
        import aws_sdk_datazone.types.resource_list

        out["provisioned_resources"] = (
            aws_sdk_datazone.types.resource_list.deserialize_json(
                data["provisionedResources"]
            )
        )
    if "status" in data:
        import aws_sdk_datazone.types.environment_status

        out["status"] = aws_sdk_datazone.types.environment_status.deserialize_json(
            data["status"]
        )
    if "environmentActions" in data:
        import aws_sdk_datazone.types.environment_action_list

        out["environment_actions"] = (
            aws_sdk_datazone.types.environment_action_list.deserialize_json(
                data["environmentActions"]
            )
        )
    if "glossaryTerms" in data:
        import aws_sdk_datazone.types.glossary_terms

        out["glossary_terms"] = aws_sdk_datazone.types.glossary_terms.deserialize_json(
            data["glossaryTerms"]
        )
    if "userParameters" in data:
        import aws_sdk_datazone.types.custom_parameter_list

        out["user_parameters"] = (
            aws_sdk_datazone.types.custom_parameter_list.deserialize_json(
                data["userParameters"]
            )
        )
    if "lastDeployment" in data:
        import aws_sdk_datazone.types.deployment

        out["last_deployment"] = aws_sdk_datazone.types.deployment.deserialize_json(
            data["lastDeployment"]
        )
    if "provisioningProperties" in data:
        import aws_sdk_datazone.types.provisioning_properties

        out["provisioning_properties"] = (
            aws_sdk_datazone.types.provisioning_properties.deserialize_json(
                data["provisioningProperties"]
            )
        )
    if "deploymentProperties" in data:
        import aws_sdk_datazone.types.deployment_properties

        out["deployment_properties"] = (
            aws_sdk_datazone.types.deployment_properties.deserialize_json(
                data["deploymentProperties"]
            )
        )
    if "environmentBlueprintId" in data:
        out["environment_blueprint_id"] = data["environmentBlueprintId"]
    if "environmentConfigurationId" in data:
        out["environment_configuration_id"] = data["environmentConfigurationId"]
    if "environmentConfigurationName" in data:
        out["environment_configuration_name"] = data["environmentConfigurationName"]
    return out
