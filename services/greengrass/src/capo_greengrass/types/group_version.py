"""Generated from Smithy shape ``com.amazonaws.greengrass#GroupVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string


class GroupVersion(TypedDict, closed=True):
    connector_definition_version_arn: NotRequired[
        "capo_greengrass.types.__string.__string"
    ]
    """The ARN of the connector definition version for this group."""
    core_definition_version_arn: NotRequired["capo_greengrass.types.__string.__string"]
    """The ARN of the core definition version for this group."""
    device_definition_version_arn: NotRequired[
        "capo_greengrass.types.__string.__string"
    ]
    """The ARN of the device definition version for this group."""
    function_definition_version_arn: NotRequired[
        "capo_greengrass.types.__string.__string"
    ]
    """The ARN of the function definition version for this group."""
    logger_definition_version_arn: NotRequired[
        "capo_greengrass.types.__string.__string"
    ]
    """The ARN of the logger definition version for this group."""
    resource_definition_version_arn: NotRequired[
        "capo_greengrass.types.__string.__string"
    ]
    """The ARN of the resource definition version for this group."""
    subscription_definition_version_arn: NotRequired[
        "capo_greengrass.types.__string.__string"
    ]
    """The ARN of the subscription definition version for this group."""


# --- restJson1 ser/de ---
def serialize_json(value: GroupVersion) -> dict:
    out: dict = {}
    if "connector_definition_version_arn" in value:
        out["ConnectorDefinitionVersionArn"] = value["connector_definition_version_arn"]
    if "core_definition_version_arn" in value:
        out["CoreDefinitionVersionArn"] = value["core_definition_version_arn"]
    if "device_definition_version_arn" in value:
        out["DeviceDefinitionVersionArn"] = value["device_definition_version_arn"]
    if "function_definition_version_arn" in value:
        out["FunctionDefinitionVersionArn"] = value["function_definition_version_arn"]
    if "logger_definition_version_arn" in value:
        out["LoggerDefinitionVersionArn"] = value["logger_definition_version_arn"]
    if "resource_definition_version_arn" in value:
        out["ResourceDefinitionVersionArn"] = value["resource_definition_version_arn"]
    if "subscription_definition_version_arn" in value:
        out["SubscriptionDefinitionVersionArn"] = value[
            "subscription_definition_version_arn"
        ]
    return out


def deserialize_json(data: dict) -> GroupVersion:
    out: GroupVersion = {}  # type: ignore[typeddict-item]
    if "ConnectorDefinitionVersionArn" in data:
        out["connector_definition_version_arn"] = data["ConnectorDefinitionVersionArn"]
    if "CoreDefinitionVersionArn" in data:
        out["core_definition_version_arn"] = data["CoreDefinitionVersionArn"]
    if "DeviceDefinitionVersionArn" in data:
        out["device_definition_version_arn"] = data["DeviceDefinitionVersionArn"]
    if "FunctionDefinitionVersionArn" in data:
        out["function_definition_version_arn"] = data["FunctionDefinitionVersionArn"]
    if "LoggerDefinitionVersionArn" in data:
        out["logger_definition_version_arn"] = data["LoggerDefinitionVersionArn"]
    if "ResourceDefinitionVersionArn" in data:
        out["resource_definition_version_arn"] = data["ResourceDefinitionVersionArn"]
    if "SubscriptionDefinitionVersionArn" in data:
        out["subscription_definition_version_arn"] = data[
            "SubscriptionDefinitionVersionArn"
        ]
    return out
