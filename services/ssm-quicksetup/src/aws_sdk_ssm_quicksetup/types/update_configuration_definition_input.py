"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#UpdateConfigurationDefinitionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm_quicksetup.types.configuration_parameters_map
    import aws_sdk_ssm_quicksetup.types.iam_role_arn


class UpdateConfigurationDefinitionInput(TypedDict):
    manager_arn: "str"
    """<p>The ARN of the configuration manager associated with the definition to update.</p>"""
    id: "str"
    """<p>The ID of the configuration definition you want to update.</p>"""
    type_version: NotRequired["str"]
    """<p>The version of the Quick Setup type to use.</p>"""
    parameters: NotRequired[
        "aws_sdk_ssm_quicksetup.types.configuration_parameters_map.ConfigurationParametersMap"
    ]
    """<p>The parameters for the configuration definition type.</p>"""
    local_deployment_execution_role_name: NotRequired["str"]
    """<p>The name of the IAM role used to deploy local configurations.</p>"""
    local_deployment_administration_role_arn: NotRequired[
        "aws_sdk_ssm_quicksetup.types.iam_role_arn.IAMRoleArn"
    ]
    """<p>The ARN of the IAM role used to administrate local configuration deployments.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfigurationDefinitionInput) -> dict:
    out: dict = {}
    if "type_version" in value:
        out["TypeVersion"] = value["type_version"]
    if "parameters" in value:
        import aws_sdk_ssm_quicksetup.types.configuration_parameters_map

        out["Parameters"] = (
            aws_sdk_ssm_quicksetup.types.configuration_parameters_map.serialize_json(
                value["parameters"]
            )
        )
    if "local_deployment_execution_role_name" in value:
        out["LocalDeploymentExecutionRoleName"] = value[
            "local_deployment_execution_role_name"
        ]
    if "local_deployment_administration_role_arn" in value:
        out["LocalDeploymentAdministrationRoleArn"] = value[
            "local_deployment_administration_role_arn"
        ]
    return out


def deserialize_json(data: dict) -> UpdateConfigurationDefinitionInput:
    out: UpdateConfigurationDefinitionInput = {}  # type: ignore[typeddict-item]
    if "TypeVersion" in data:
        out["type_version"] = data["TypeVersion"]
    if "Parameters" in data:
        import aws_sdk_ssm_quicksetup.types.configuration_parameters_map

        out["parameters"] = (
            aws_sdk_ssm_quicksetup.types.configuration_parameters_map.deserialize_json(
                data["Parameters"]
            )
        )
    if "LocalDeploymentExecutionRoleName" in data:
        out["local_deployment_execution_role_name"] = data[
            "LocalDeploymentExecutionRoleName"
        ]
    if "LocalDeploymentAdministrationRoleArn" in data:
        out["local_deployment_administration_role_arn"] = data[
            "LocalDeploymentAdministrationRoleArn"
        ]
    return out
