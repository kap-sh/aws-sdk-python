"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#ConfigurationDefinition``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ssm_quicksetup.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_ssm_quicksetup.types.configuration_parameters_map
    import aws_sdk_ssm_quicksetup.types.iam_role_arn

class ConfigurationDefinition(TypedDict):
    type: "str"
    """<p>The type of the Quick Setup configuration.</p>"""
    parameters: "aws_sdk_ssm_quicksetup.types.configuration_parameters_map.ConfigurationParametersMap"
    """<p>A list of key-value pairs containing the required parameters for the configuration type.</p>"""
    type_version: NotRequired["str"]
    """<p>The version of the Quick Setup type used.</p>"""
    local_deployment_execution_role_name: NotRequired["str"]
    """<p>The name of the IAM role used to deploy local configurations.</p>"""
    local_deployment_administration_role_arn: NotRequired["aws_sdk_ssm_quicksetup.types.iam_role_arn.IAMRoleArn"]
    """<p>The ARN of the IAM role used to administrate local configuration deployments.</p>"""
    id: NotRequired["str"]
    """<p>The ID of the configuration definition.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationDefinition) -> dict:
    out: dict = {}
    out["Type"] = value["type"]
    import aws_sdk_ssm_quicksetup.types.configuration_parameters_map
    out["Parameters"] = aws_sdk_ssm_quicksetup.types.configuration_parameters_map.serialize_json(value["parameters"])
    if "type_version" in value:
        out["TypeVersion"] = value["type_version"]
    if "local_deployment_execution_role_name" in value:
        out["LocalDeploymentExecutionRoleName"] = value["local_deployment_execution_role_name"]
    if "local_deployment_administration_role_arn" in value:
        out["LocalDeploymentAdministrationRoleArn"] = value["local_deployment_administration_role_arn"]
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> ConfigurationDefinition:
    out: ConfigurationDefinition = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    else:
        raise DeserializationError("ConfigurationDefinition.type required")
    if "Parameters" in data:
        import aws_sdk_ssm_quicksetup.types.configuration_parameters_map
        out["parameters"] = aws_sdk_ssm_quicksetup.types.configuration_parameters_map.deserialize_json(data["Parameters"])
    else:
        raise DeserializationError("ConfigurationDefinition.parameters required")
    if "TypeVersion" in data:
        out["type_version"] = data["TypeVersion"]
    if "LocalDeploymentExecutionRoleName" in data:
        out["local_deployment_execution_role_name"] = data["LocalDeploymentExecutionRoleName"]
    if "LocalDeploymentAdministrationRoleArn" in data:
        out["local_deployment_administration_role_arn"] = data["LocalDeploymentAdministrationRoleArn"]
    if "Id" in data:
        out["id"] = data["Id"]
    return out