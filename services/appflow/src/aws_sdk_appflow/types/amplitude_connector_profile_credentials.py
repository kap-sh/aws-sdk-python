"""Generated from Smithy shape ``com.amazonaws.appflow#AmplitudeConnectorProfileCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.api_key
    import aws_sdk_appflow.types.secret_key


class AmplitudeConnectorProfileCredentials(TypedDict, closed=True):
    api_key: "aws_sdk_appflow.types.api_key.ApiKey"
    """<p> A unique alphanumeric identifier used to authenticate a user, developer, or calling program to your API. </p>"""
    secret_key: "aws_sdk_appflow.types.secret_key.SecretKey"
    """<p> The Secret Access Key portion of the credentials. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmplitudeConnectorProfileCredentials) -> dict:
    out: dict = {}
    out["apiKey"] = value["api_key"]
    out["secretKey"] = value["secret_key"]
    return out


def deserialize_json(data: dict) -> AmplitudeConnectorProfileCredentials:
    out: AmplitudeConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
    if "apiKey" in data:
        out["api_key"] = data["apiKey"]
    else:
        raise DeserializationError(
            "AmplitudeConnectorProfileCredentials.api_key required"
        )
    if "secretKey" in data:
        out["secret_key"] = data["secretKey"]
    else:
        raise DeserializationError(
            "AmplitudeConnectorProfileCredentials.secret_key required"
        )
    return out
