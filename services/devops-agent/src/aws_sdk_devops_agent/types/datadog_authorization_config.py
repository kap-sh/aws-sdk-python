"""Generated from Smithy shape ``com.amazonaws.devopsagent#DatadogAuthorizationConfig``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.mcp_server_authorization_discovery_config


class _DatadogAuthorizationConfig_authorizationDiscovery(TypedDict):
    authorizationDiscovery: "aws_sdk_devops_agent.types.mcp_server_authorization_discovery_config.MCPServerAuthorizationDiscoveryConfig"


DatadogAuthorizationConfig: TypeAlias = (
    _DatadogAuthorizationConfig_authorizationDiscovery
)


# --- restJson1 ser/de ---
def serialize_json(value: DatadogAuthorizationConfig) -> dict:
    if "authorizationDiscovery" in value:
        import aws_sdk_devops_agent.types.mcp_server_authorization_discovery_config

        return {
            "authorizationDiscovery": aws_sdk_devops_agent.types.mcp_server_authorization_discovery_config.serialize_json(
                value["authorizationDiscovery"]
            )
        }
    else:
        raise SerializationError("DatadogAuthorizationConfig: no variant present")


def deserialize_json(data: dict) -> DatadogAuthorizationConfig:
    if "authorizationDiscovery" in data:
        import aws_sdk_devops_agent.types.mcp_server_authorization_discovery_config

        return {
            "authorizationDiscovery": aws_sdk_devops_agent.types.mcp_server_authorization_discovery_config.deserialize_json(
                data["authorizationDiscovery"]
            )
        }
    else:
        raise DeserializationError(
            "DatadogAuthorizationConfig: no recognized variant key"
        )
