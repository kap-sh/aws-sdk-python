"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.account_pool_list
    import aws_sdk_datazone.types.aws_account
    import aws_sdk_datazone.types.deployment_mode
    import aws_sdk_datazone.types.deployment_order
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.environment_blueprint_id
    import aws_sdk_datazone.types.environment_configuration_id
    import aws_sdk_datazone.types.environment_configuration_name
    import aws_sdk_datazone.types.environment_configuration_parameters_details
    import aws_sdk_datazone.types.region


class EnvironmentConfiguration(TypedDict):
    name: "aws_sdk_datazone.types.environment_configuration_name.EnvironmentConfigurationName"
    """<p>The environment name.</p>"""
    id: NotRequired[
        "aws_sdk_datazone.types.environment_configuration_id.EnvironmentConfigurationId"
    ]
    """<p>The environment ID.</p>"""
    environment_blueprint_id: (
        "aws_sdk_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
    )
    """<p>The environment blueprint ID.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The environment description.</p>"""
    deployment_mode: NotRequired[
        "aws_sdk_datazone.types.deployment_mode.DeploymentMode"
    ]
    """<p>The deployment mode of the environment.</p>"""
    configuration_parameters: NotRequired[
        "aws_sdk_datazone.types.environment_configuration_parameters_details.EnvironmentConfigurationParametersDetails"
    ]
    """<p>The configuration parameters of the environment.</p>"""
    aws_account: NotRequired["aws_sdk_datazone.types.aws_account.AwsAccount"]
    """<p>The Amazon Web Services account of the environment.</p>"""
    account_pools: NotRequired[
        "aws_sdk_datazone.types.account_pool_list.AccountPoolList"
    ]
    """<p>The account pools used by a custom project profile.</p>"""
    aws_region: NotRequired["aws_sdk_datazone.types.region.Region"]
    """<p>The Amazon Web Services Region of the environment.</p>"""
    deployment_order: NotRequired[
        "aws_sdk_datazone.types.deployment_order.DeploymentOrder"
    ]
    """<p>The deployment order of the environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentConfiguration) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "id" in value:
        out["id"] = value["id"]
    out["environmentBlueprintId"] = value["environment_blueprint_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "deployment_mode" in value:
        import aws_sdk_datazone.types.deployment_mode

        out["deploymentMode"] = aws_sdk_datazone.types.deployment_mode.serialize_json(
            value["deployment_mode"]
        )
    if "configuration_parameters" in value:
        import aws_sdk_datazone.types.environment_configuration_parameters_details

        out["configurationParameters"] = (
            aws_sdk_datazone.types.environment_configuration_parameters_details.serialize_json(
                value["configuration_parameters"]
            )
        )
    if "aws_account" in value:
        import aws_sdk_datazone.types.aws_account

        out["awsAccount"] = aws_sdk_datazone.types.aws_account.serialize_json(
            value["aws_account"]
        )
    if "account_pools" in value:
        import aws_sdk_datazone.types.account_pool_list

        out["accountPools"] = aws_sdk_datazone.types.account_pool_list.serialize_json(
            value["account_pools"]
        )
    if "aws_region" in value:
        import aws_sdk_datazone.types.region

        out["awsRegion"] = aws_sdk_datazone.types.region.serialize_json(
            value["aws_region"]
        )
    if "deployment_order" in value:
        out["deploymentOrder"] = value["deployment_order"]
    return out


def deserialize_json(data: dict) -> EnvironmentConfiguration:
    out: EnvironmentConfiguration = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("EnvironmentConfiguration.name required")
    if "id" in data:
        out["id"] = data["id"]
    if "environmentBlueprintId" in data:
        out["environment_blueprint_id"] = data["environmentBlueprintId"]
    else:
        raise DeserializationError(
            "EnvironmentConfiguration.environment_blueprint_id required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "deploymentMode" in data:
        import aws_sdk_datazone.types.deployment_mode

        out["deployment_mode"] = (
            aws_sdk_datazone.types.deployment_mode.deserialize_json(
                data["deploymentMode"]
            )
        )
    if "configurationParameters" in data:
        import aws_sdk_datazone.types.environment_configuration_parameters_details

        out["configuration_parameters"] = (
            aws_sdk_datazone.types.environment_configuration_parameters_details.deserialize_json(
                data["configurationParameters"]
            )
        )
    if "awsAccount" in data:
        import aws_sdk_datazone.types.aws_account

        out["aws_account"] = aws_sdk_datazone.types.aws_account.deserialize_json(
            data["awsAccount"]
        )
    if "accountPools" in data:
        import aws_sdk_datazone.types.account_pool_list

        out["account_pools"] = (
            aws_sdk_datazone.types.account_pool_list.deserialize_json(
                data["accountPools"]
            )
        )
    if "awsRegion" in data:
        import aws_sdk_datazone.types.region

        out["aws_region"] = aws_sdk_datazone.types.region.deserialize_json(
            data["awsRegion"]
        )
    if "deploymentOrder" in data:
        out["deployment_order"] = data["deploymentOrder"]
    return out
