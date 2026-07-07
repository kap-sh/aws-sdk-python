"""Generated from Smithy shape ``com.amazonaws.greengrassv2#DeploymentPolicies``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.deployment_component_update_policy
    import aws_sdk_greengrassv2.types.deployment_configuration_validation_policy
    import aws_sdk_greengrassv2.types.deployment_failure_handling_policy


class DeploymentPolicies(TypedDict, closed=True):
    failure_handling_policy: NotRequired[
        "aws_sdk_greengrassv2.types.deployment_failure_handling_policy.DeploymentFailureHandlingPolicy"
    ]
    """<p>The failure handling policy for the configuration deployment. This policy defines what to do if the deployment fails.</p> <p>Default: <code>ROLLBACK</code> </p>"""
    component_update_policy: NotRequired[
        "aws_sdk_greengrassv2.types.deployment_component_update_policy.DeploymentComponentUpdatePolicy"
    ]
    """<p>The component update policy for the configuration deployment. This policy defines when it's safe to deploy the configuration to devices.</p>"""
    configuration_validation_policy: NotRequired[
        "aws_sdk_greengrassv2.types.deployment_configuration_validation_policy.DeploymentConfigurationValidationPolicy"
    ]
    """<p>The configuration validation policy for the configuration deployment. This policy defines how long each component has to validate its configure updates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentPolicies) -> dict:
    out: dict = {}
    if "failure_handling_policy" in value:
        import aws_sdk_greengrassv2.types.deployment_failure_handling_policy

        out["failureHandlingPolicy"] = (
            aws_sdk_greengrassv2.types.deployment_failure_handling_policy.serialize_json(
                value["failure_handling_policy"]
            )
        )
    if "component_update_policy" in value:
        import aws_sdk_greengrassv2.types.deployment_component_update_policy

        out["componentUpdatePolicy"] = (
            aws_sdk_greengrassv2.types.deployment_component_update_policy.serialize_json(
                value["component_update_policy"]
            )
        )
    if "configuration_validation_policy" in value:
        import aws_sdk_greengrassv2.types.deployment_configuration_validation_policy

        out["configurationValidationPolicy"] = (
            aws_sdk_greengrassv2.types.deployment_configuration_validation_policy.serialize_json(
                value["configuration_validation_policy"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeploymentPolicies:
    out: DeploymentPolicies = {}  # type: ignore[typeddict-item]
    if "failureHandlingPolicy" in data:
        import aws_sdk_greengrassv2.types.deployment_failure_handling_policy

        out["failure_handling_policy"] = (
            aws_sdk_greengrassv2.types.deployment_failure_handling_policy.deserialize_json(
                data["failureHandlingPolicy"]
            )
        )
    if "componentUpdatePolicy" in data:
        import aws_sdk_greengrassv2.types.deployment_component_update_policy

        out["component_update_policy"] = (
            aws_sdk_greengrassv2.types.deployment_component_update_policy.deserialize_json(
                data["componentUpdatePolicy"]
            )
        )
    if "configurationValidationPolicy" in data:
        import aws_sdk_greengrassv2.types.deployment_configuration_validation_policy

        out["configuration_validation_policy"] = (
            aws_sdk_greengrassv2.types.deployment_configuration_validation_policy.deserialize_json(
                data["configurationValidationPolicy"]
            )
        )
    return out
