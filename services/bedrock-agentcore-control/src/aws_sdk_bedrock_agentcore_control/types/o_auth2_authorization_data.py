"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#OAuth2AuthorizationData``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError


class OAuth2AuthorizationData(TypedDict, closed=True):
    authorization_url: "str"
    """<p>The URL to initiate the authorization process. This URL is provided when the OAuth2 access token requires user authorization.</p>"""
    user_id: NotRequired["str"]
    """<p>The user identifier associated with the OAuth2 authorization session that is defined by AgentCore Gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OAuth2AuthorizationData) -> dict:
    out: dict = {}
    out["authorizationUrl"] = value["authorization_url"]
    if "user_id" in value:
        out["userId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> OAuth2AuthorizationData:
    out: OAuth2AuthorizationData = {}  # type: ignore[typeddict-item]
    if "authorizationUrl" in data:
        out["authorization_url"] = data["authorizationUrl"]
    else:
        raise DeserializationError("OAuth2AuthorizationData.authorization_url required")
    if "userId" in data:
        out["user_id"] = data["userId"]
    return out
