"""Generated from Smithy shape ``com.amazonaws.appfabric#Oauth2Credential``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.sensitive_string2048
    import aws_sdk_appfabric.types.string2048


class Oauth2Credential(TypedDict, closed=True):
    client_id: "aws_sdk_appfabric.types.string2048.String2048"
    """<p>The client ID of the client application.</p>"""
    client_secret: "aws_sdk_appfabric.types.sensitive_string2048.SensitiveString2048"
    """<p>The client secret of the client application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Oauth2Credential) -> dict:
    out: dict = {}
    out["clientId"] = value["client_id"]
    out["clientSecret"] = value["client_secret"]
    return out


def deserialize_json(data: dict) -> Oauth2Credential:
    out: Oauth2Credential = {}  # type: ignore[typeddict-item]
    if "clientId" in data:
        out["client_id"] = data["clientId"]
    else:
        raise DeserializationError("Oauth2Credential.client_id required")
    if "clientSecret" in data:
        out["client_secret"] = data["clientSecret"]
    else:
        raise DeserializationError("Oauth2Credential.client_secret required")
    return out
