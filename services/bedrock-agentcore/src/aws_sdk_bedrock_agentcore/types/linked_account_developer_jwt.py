"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#LinkedAccountDeveloperJwt``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.jwt_key_id


class LinkedAccountDeveloperJwt(TypedDict):
    kid: "aws_sdk_bedrock_agentcore.types.jwt_key_id.JwtKeyId"
    """<p>The key ID (kid) from the JWT header. Identifies which key was used to sign the JWT.</p>"""
    sub: "str"
    """<p>The subject (sub) claim from the JWT payload. Identifies the principal that is the subject of the JWT.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LinkedAccountDeveloperJwt) -> dict:
    out: dict = {}
    out["kid"] = value["kid"]
    out["sub"] = value["sub"]
    return out


def deserialize_json(data: dict) -> LinkedAccountDeveloperJwt:
    out: LinkedAccountDeveloperJwt = {}  # type: ignore[typeddict-item]
    if "kid" in data:
        out["kid"] = data["kid"]
    else:
        raise DeserializationError("LinkedAccountDeveloperJwt.kid required")
    if "sub" in data:
        out["sub"] = data["sub"]
    else:
        raise DeserializationError("LinkedAccountDeveloperJwt.sub required")
    return out
