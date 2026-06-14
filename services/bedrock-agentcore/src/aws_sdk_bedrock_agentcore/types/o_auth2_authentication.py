"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#OAuth2Authentication``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.email


class OAuth2Authentication(TypedDict):
    sub: "str"
    """<p>The subject (sub) claim from the OAuth2 provider. Uniquely identifies the user at the provider.</p>"""
    email_address: NotRequired["aws_sdk_bedrock_agentcore.types.email.Email"]
    """<p>The email address from the OAuth2 provider.</p>"""
    name: NotRequired["str"]
    """<p>The user's name from the OAuth2 provider.</p>"""
    username: NotRequired["str"]
    """<p>The username from the OAuth2 provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OAuth2Authentication) -> dict:
    out: dict = {}
    out["sub"] = value["sub"]
    if "email_address" in value:
        out["emailAddress"] = value["email_address"]
    if "name" in value:
        out["name"] = value["name"]
    if "username" in value:
        out["username"] = value["username"]
    return out


def deserialize_json(data: dict) -> OAuth2Authentication:
    out: OAuth2Authentication = {}  # type: ignore[typeddict-item]
    if "sub" in data:
        out["sub"] = data["sub"]
    else:
        raise DeserializationError("OAuth2Authentication.sub required")
    if "emailAddress" in data:
        out["email_address"] = data["emailAddress"]
    if "name" in data:
        out["name"] = data["name"]
    if "username" in data:
        out["username"] = data["username"]
    return out
