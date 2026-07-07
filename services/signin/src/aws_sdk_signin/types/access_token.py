"""Generated from Smithy shape ``com.amazonaws.signin#AccessToken``."""

from typing_extensions import TypedDict

from aws_sdk_signin.errors import DeserializationError


class AccessToken(TypedDict, closed=True):
    access_key_id: "str"
    """AWS access key ID for temporary credentials"""
    secret_access_key: "str"
    """AWS secret access key for temporary credentials"""
    session_token: "str"
    """AWS session token for temporary credentials"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessToken) -> dict:
    out: dict = {}
    out["accessKeyId"] = value["access_key_id"]
    out["secretAccessKey"] = value["secret_access_key"]
    out["sessionToken"] = value["session_token"]
    return out


def deserialize_json(data: dict) -> AccessToken:
    out: AccessToken = {}  # type: ignore[typeddict-item]
    if "accessKeyId" in data:
        out["access_key_id"] = data["accessKeyId"]
    else:
        raise DeserializationError("AccessToken.access_key_id required")
    if "secretAccessKey" in data:
        out["secret_access_key"] = data["secretAccessKey"]
    else:
        raise DeserializationError("AccessToken.secret_access_key required")
    if "sessionToken" in data:
        out["session_token"] = data["sessionToken"]
    else:
        raise DeserializationError("AccessToken.session_token required")
    return out
