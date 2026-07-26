"""Generated from Smithy shape ``com.amazonaws.devopsagent#MCPServerOAuth3LOConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.client_id
    import capo_devops_agent.types.client_secret
    import capo_devops_agent.types.exchange_parameters
    import capo_devops_agent.types.scopes


class MCPServerOAuth3LOConfig(TypedDict, closed=True):
    client_name: NotRequired["str"]
    """<p>User friendly OAuth client name specified by end user.</p>"""
    client_id: "capo_devops_agent.types.client_id.ClientId"
    """<p>OAuth client ID for authenticating with the service.</p>"""
    exchange_parameters: NotRequired[
        "capo_devops_agent.types.exchange_parameters.ExchangeParameters"
    ]
    """<p>OAuth token exchange parameters for authenticating with the service.</p>"""
    return_to_endpoint: "str"
    """<p>The endpoint to return to after OAuth flow completes (must be AWS console domain)</p>"""
    authorization_url: "str"
    """<p>OAuth authorization URL for 3LO authentication.</p>"""
    exchange_url: "str"
    """<p>OAuth token exchange URL.</p>"""
    client_secret: NotRequired["capo_devops_agent.types.client_secret.ClientSecret"]
    """<p>OAuth client secret for authenticating with the service. Required for confidential clients or when PKCE is not supported. Optional for public clients using PKCE.</p>"""
    support_code_challenge: "bool"
    """<p>Whether the service supports PKCE (Proof Key for Code Exchange) for enhanced security during the OAuth flow.</p>"""
    scopes: NotRequired["capo_devops_agent.types.scopes.Scopes"]
    """<p>OAuth scopes for 3LO authentication. The service will always request scope offline_access.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MCPServerOAuth3LOConfig) -> dict:
    out: dict = {}
    if "client_name" in value:
        out["clientName"] = value["client_name"]
    out["clientId"] = value["client_id"]
    if "exchange_parameters" in value:
        import capo_devops_agent.types.exchange_parameters

        out["exchangeParameters"] = (
            capo_devops_agent.types.exchange_parameters.serialize_json(
                value["exchange_parameters"]
            )
        )
    out["returnToEndpoint"] = value["return_to_endpoint"]
    out["authorizationUrl"] = value["authorization_url"]
    out["exchangeUrl"] = value["exchange_url"]
    if "client_secret" in value:
        out["clientSecret"] = value["client_secret"]
    out["supportCodeChallenge"] = value.get("support_code_challenge", False)
    if "scopes" in value:
        import capo_devops_agent.types.scopes

        out["scopes"] = capo_devops_agent.types.scopes.serialize_json(value["scopes"])
    return out


def deserialize_json(data: dict) -> MCPServerOAuth3LOConfig:
    out: MCPServerOAuth3LOConfig = {}  # type: ignore[typeddict-item]
    if "clientName" in data:
        out["client_name"] = data["clientName"]
    if "clientId" in data:
        out["client_id"] = data["clientId"]
    else:
        raise DeserializationError("MCPServerOAuth3LOConfig.client_id required")
    if "exchangeParameters" in data:
        import capo_devops_agent.types.exchange_parameters

        out["exchange_parameters"] = (
            capo_devops_agent.types.exchange_parameters.deserialize_json(
                data["exchangeParameters"]
            )
        )
    if "returnToEndpoint" in data:
        out["return_to_endpoint"] = data["returnToEndpoint"]
    else:
        raise DeserializationError(
            "MCPServerOAuth3LOConfig.return_to_endpoint required"
        )
    if "authorizationUrl" in data:
        out["authorization_url"] = data["authorizationUrl"]
    else:
        raise DeserializationError("MCPServerOAuth3LOConfig.authorization_url required")
    if "exchangeUrl" in data:
        out["exchange_url"] = data["exchangeUrl"]
    else:
        raise DeserializationError("MCPServerOAuth3LOConfig.exchange_url required")
    if "clientSecret" in data:
        out["client_secret"] = data["clientSecret"]
    if "supportCodeChallenge" in data:
        out["support_code_challenge"] = data["supportCodeChallenge"]
    else:
        out["support_code_challenge"] = False
    if "scopes" in data:
        import capo_devops_agent.types.scopes

        out["scopes"] = capo_devops_agent.types.scopes.deserialize_json(data["scopes"])
    return out
