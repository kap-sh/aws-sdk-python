"""Generated from Smithy shape ``com.amazonaws.devopsagent#MCPServerAuthorizationConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_devops_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.mcp_server_api_key_config
    import aws_sdk_devops_agent.types.mcp_server_authorization_discovery_config
    import aws_sdk_devops_agent.types.mcp_server_bearer_token_config
    import aws_sdk_devops_agent.types.mcp_server_o_auth3_lo_config
    import aws_sdk_devops_agent.types.mcp_server_o_auth_client_credentials_config


class _MCPServerAuthorizationConfig_oAuthClientCredentials(TypedDict, closed=True):
    oAuthClientCredentials: "aws_sdk_devops_agent.types.mcp_server_o_auth_client_credentials_config.MCPServerOAuthClientCredentialsConfig"


class _MCPServerAuthorizationConfig_oAuth3LO(TypedDict, closed=True):
    oAuth3LO: "aws_sdk_devops_agent.types.mcp_server_o_auth3_lo_config.MCPServerOAuth3LOConfig"


class _MCPServerAuthorizationConfig_apiKey(TypedDict, closed=True):
    apiKey: "aws_sdk_devops_agent.types.mcp_server_api_key_config.MCPServerAPIKeyConfig"


class _MCPServerAuthorizationConfig_bearerToken(TypedDict, closed=True):
    bearerToken: "aws_sdk_devops_agent.types.mcp_server_bearer_token_config.MCPServerBearerTokenConfig"


class _MCPServerAuthorizationConfig_authorizationDiscovery(TypedDict, closed=True):
    authorizationDiscovery: "aws_sdk_devops_agent.types.mcp_server_authorization_discovery_config.MCPServerAuthorizationDiscoveryConfig"


MCPServerAuthorizationConfig: TypeAlias = (
    _MCPServerAuthorizationConfig_oAuthClientCredentials
    | _MCPServerAuthorizationConfig_oAuth3LO
    | _MCPServerAuthorizationConfig_apiKey
    | _MCPServerAuthorizationConfig_bearerToken
    | _MCPServerAuthorizationConfig_authorizationDiscovery
)


# --- restJson1 ser/de ---
def serialize_json(value: MCPServerAuthorizationConfig) -> dict:
    if "oAuthClientCredentials" in value:
        import aws_sdk_devops_agent.types.mcp_server_o_auth_client_credentials_config

        return {
            "oAuthClientCredentials": aws_sdk_devops_agent.types.mcp_server_o_auth_client_credentials_config.serialize_json(
                value["oAuthClientCredentials"]
            )
        }
    elif "oAuth3LO" in value:
        import aws_sdk_devops_agent.types.mcp_server_o_auth3_lo_config

        return {
            "oAuth3LO": aws_sdk_devops_agent.types.mcp_server_o_auth3_lo_config.serialize_json(
                value["oAuth3LO"]
            )
        }
    elif "apiKey" in value:
        import aws_sdk_devops_agent.types.mcp_server_api_key_config

        return {
            "apiKey": aws_sdk_devops_agent.types.mcp_server_api_key_config.serialize_json(
                value["apiKey"]
            )
        }
    elif "bearerToken" in value:
        import aws_sdk_devops_agent.types.mcp_server_bearer_token_config

        return {
            "bearerToken": aws_sdk_devops_agent.types.mcp_server_bearer_token_config.serialize_json(
                value["bearerToken"]
            )
        }
    elif "authorizationDiscovery" in value:
        import aws_sdk_devops_agent.types.mcp_server_authorization_discovery_config

        return {
            "authorizationDiscovery": aws_sdk_devops_agent.types.mcp_server_authorization_discovery_config.serialize_json(
                value["authorizationDiscovery"]
            )
        }
    else:
        raise SerializationError("MCPServerAuthorizationConfig: no variant present")


def deserialize_json(data: dict) -> MCPServerAuthorizationConfig:
    if "oAuthClientCredentials" in data:
        import aws_sdk_devops_agent.types.mcp_server_o_auth_client_credentials_config

        return {
            "oAuthClientCredentials": aws_sdk_devops_agent.types.mcp_server_o_auth_client_credentials_config.deserialize_json(
                data["oAuthClientCredentials"]
            )
        }
    elif "oAuth3LO" in data:
        import aws_sdk_devops_agent.types.mcp_server_o_auth3_lo_config

        return {
            "oAuth3LO": aws_sdk_devops_agent.types.mcp_server_o_auth3_lo_config.deserialize_json(
                data["oAuth3LO"]
            )
        }
    elif "apiKey" in data:
        import aws_sdk_devops_agent.types.mcp_server_api_key_config

        return {
            "apiKey": aws_sdk_devops_agent.types.mcp_server_api_key_config.deserialize_json(
                data["apiKey"]
            )
        }
    elif "bearerToken" in data:
        import aws_sdk_devops_agent.types.mcp_server_bearer_token_config

        return {
            "bearerToken": aws_sdk_devops_agent.types.mcp_server_bearer_token_config.deserialize_json(
                data["bearerToken"]
            )
        }
    elif "authorizationDiscovery" in data:
        import aws_sdk_devops_agent.types.mcp_server_authorization_discovery_config

        return {
            "authorizationDiscovery": aws_sdk_devops_agent.types.mcp_server_authorization_discovery_config.deserialize_json(
                data["authorizationDiscovery"]
            )
        }
    else:
        raise DeserializationError(
            "MCPServerAuthorizationConfig: no recognized variant key"
        )
