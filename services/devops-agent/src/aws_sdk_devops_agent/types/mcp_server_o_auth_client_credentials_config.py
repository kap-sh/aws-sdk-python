"""Generated from Smithy shape ``com.amazonaws.devopsagent#MCPServerOAuthClientCredentialsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.client_id
    import aws_sdk_devops_agent.types.client_secret
    import aws_sdk_devops_agent.types.exchange_parameters
    import aws_sdk_devops_agent.types.scopes


class MCPServerOAuthClientCredentialsConfig(TypedDict, closed=True):
    client_name: NotRequired["str"]
    """<p>User friendly OAuth client name specified by end user.</p>"""
    client_id: "aws_sdk_devops_agent.types.client_id.ClientId"
    """<p>OAuth client ID for authenticating with the service.</p>"""
    exchange_parameters: NotRequired[
        "aws_sdk_devops_agent.types.exchange_parameters.ExchangeParameters"
    ]
    """<p>OAuth token exchange parameters for authenticating with the service.</p>"""
    client_secret: "aws_sdk_devops_agent.types.client_secret.ClientSecret"
    """<p>OAuth client secret for authenticating with the service.</p>"""
    exchange_url: "str"
    """<p>OAuth token exchange URL.</p>"""
    scopes: NotRequired["aws_sdk_devops_agent.types.scopes.Scopes"]
    """<p>OAuth scopes for 3LO authentication. The service will always request scope offline_access.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MCPServerOAuthClientCredentialsConfig) -> dict:
    out: dict = {}
    if "client_name" in value:
        out["clientName"] = value["client_name"]
    out["clientId"] = value["client_id"]
    if "exchange_parameters" in value:
        import aws_sdk_devops_agent.types.exchange_parameters

        out["exchangeParameters"] = (
            aws_sdk_devops_agent.types.exchange_parameters.serialize_json(
                value["exchange_parameters"]
            )
        )
    out["clientSecret"] = value["client_secret"]
    out["exchangeUrl"] = value["exchange_url"]
    if "scopes" in value:
        import aws_sdk_devops_agent.types.scopes

        out["scopes"] = aws_sdk_devops_agent.types.scopes.serialize_json(
            value["scopes"]
        )
    return out


def deserialize_json(data: dict) -> MCPServerOAuthClientCredentialsConfig:
    out: MCPServerOAuthClientCredentialsConfig = {}  # type: ignore[typeddict-item]
    if "clientName" in data:
        out["client_name"] = data["clientName"]
    if "clientId" in data:
        out["client_id"] = data["clientId"]
    else:
        raise DeserializationError(
            "MCPServerOAuthClientCredentialsConfig.client_id required"
        )
    if "exchangeParameters" in data:
        import aws_sdk_devops_agent.types.exchange_parameters

        out["exchange_parameters"] = (
            aws_sdk_devops_agent.types.exchange_parameters.deserialize_json(
                data["exchangeParameters"]
            )
        )
    if "clientSecret" in data:
        out["client_secret"] = data["clientSecret"]
    else:
        raise DeserializationError(
            "MCPServerOAuthClientCredentialsConfig.client_secret required"
        )
    if "exchangeUrl" in data:
        out["exchange_url"] = data["exchangeUrl"]
    else:
        raise DeserializationError(
            "MCPServerOAuthClientCredentialsConfig.exchange_url required"
        )
    if "scopes" in data:
        import aws_sdk_devops_agent.types.scopes

        out["scopes"] = aws_sdk_devops_agent.types.scopes.deserialize_json(
            data["scopes"]
        )
    return out
