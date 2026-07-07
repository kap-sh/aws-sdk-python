"""Generated from Smithy shape ``com.amazonaws.appflow#ApiKeyCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.api_key
    import aws_sdk_appflow.types.api_secret_key


class ApiKeyCredentials(TypedDict, closed=True):
    api_key: "aws_sdk_appflow.types.api_key.ApiKey"
    """<p>The API key required for API key authentication.</p>"""
    api_secret_key: NotRequired["aws_sdk_appflow.types.api_secret_key.ApiSecretKey"]
    """<p>The API secret key required for API key authentication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiKeyCredentials) -> dict:
    out: dict = {}
    out["apiKey"] = value["api_key"]
    if "api_secret_key" in value:
        out["apiSecretKey"] = value["api_secret_key"]
    return out


def deserialize_json(data: dict) -> ApiKeyCredentials:
    out: ApiKeyCredentials = {}  # type: ignore[typeddict-item]
    if "apiKey" in data:
        out["api_key"] = data["apiKey"]
    else:
        raise DeserializationError("ApiKeyCredentials.api_key required")
    if "apiSecretKey" in data:
        out["api_secret_key"] = data["apiSecretKey"]
    return out
