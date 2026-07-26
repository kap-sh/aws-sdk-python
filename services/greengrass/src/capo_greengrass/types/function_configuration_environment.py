"""Generated from Smithy shape ``com.amazonaws.greengrass#FunctionConfigurationEnvironment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__boolean
    import capo_greengrass.types.__list_of_resource_access_policy
    import capo_greengrass.types.__map_of__string
    import capo_greengrass.types.function_execution_config


class FunctionConfigurationEnvironment(TypedDict, closed=True):
    access_sysfs: NotRequired["capo_greengrass.types.__boolean.__boolean"]
    """If true, the Lambda function is allowed to access the host's /sys folder. Use this when the Lambda function needs to read device information from /sys. This setting applies only when you run the Lambda function in a Greengrass container."""
    execution: NotRequired[
        "capo_greengrass.types.function_execution_config.FunctionExecutionConfig"
    ]
    """Configuration related to executing the Lambda function"""
    resource_access_policies: NotRequired[
        "capo_greengrass.types.__list_of_resource_access_policy.__listOfResourceAccessPolicy"
    ]
    """A list of the resources, with their permissions, to which the Lambda function will be granted access. A Lambda function can have at most 10 resources. ResourceAccessPolicies apply only when you run the Lambda function in a Greengrass container."""
    variables: NotRequired["capo_greengrass.types.__map_of__string.__mapOf__string"]
    """Environment variables for the Lambda function's configuration."""


# --- restJson1 ser/de ---
def serialize_json(value: FunctionConfigurationEnvironment) -> dict:
    out: dict = {}
    if "access_sysfs" in value:
        out["AccessSysfs"] = value["access_sysfs"]
    if "execution" in value:
        import capo_greengrass.types.function_execution_config

        out["Execution"] = (
            capo_greengrass.types.function_execution_config.serialize_json(
                value["execution"]
            )
        )
    if "resource_access_policies" in value:
        import capo_greengrass.types.__list_of_resource_access_policy

        out["ResourceAccessPolicies"] = (
            capo_greengrass.types.__list_of_resource_access_policy.serialize_json(
                value["resource_access_policies"]
            )
        )
    if "variables" in value:
        import capo_greengrass.types.__map_of__string

        out["Variables"] = capo_greengrass.types.__map_of__string.serialize_json(
            value["variables"]
        )
    return out


def deserialize_json(data: dict) -> FunctionConfigurationEnvironment:
    out: FunctionConfigurationEnvironment = {}  # type: ignore[typeddict-item]
    if "AccessSysfs" in data:
        out["access_sysfs"] = data["AccessSysfs"]
    if "Execution" in data:
        import capo_greengrass.types.function_execution_config

        out["execution"] = (
            capo_greengrass.types.function_execution_config.deserialize_json(
                data["Execution"]
            )
        )
    if "ResourceAccessPolicies" in data:
        import capo_greengrass.types.__list_of_resource_access_policy

        out["resource_access_policies"] = (
            capo_greengrass.types.__list_of_resource_access_policy.deserialize_json(
                data["ResourceAccessPolicies"]
            )
        )
    if "Variables" in data:
        import capo_greengrass.types.__map_of__string

        out["variables"] = capo_greengrass.types.__map_of__string.deserialize_json(
            data["Variables"]
        )
    return out
