"""Generated from Smithy shape ``com.amazonaws.quicksight#APIKeyConnectionMetadata``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_quicksight.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_quicksight.types.api_key
    import aws_sdk_quicksight.types.email
    import aws_sdk_quicksight.types.endpoint

class APIKeyConnectionMetadata(TypedDict):
    base_endpoint: "aws_sdk_quicksight.types.endpoint.Endpoint"
    """<p>The base URL endpoint for the external service.</p>"""
    api_key: "aws_sdk_quicksight.types.api_key.APIKey"
    """<p>The API key used for authentication.</p>"""
    email: NotRequired["aws_sdk_quicksight.types.email.Email"]
    """<p>The email address associated with the API key, if required.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: APIKeyConnectionMetadata) -> dict:
    out: dict = {}
    out["BaseEndpoint"] = value["base_endpoint"]
    out["ApiKey"] = value["api_key"]
    if "email" in value:
        out["Email"] = value["email"]
    return out


def deserialize_json(data: dict) -> APIKeyConnectionMetadata:
    out: APIKeyConnectionMetadata = {}  # type: ignore[typeddict-item]
    if "BaseEndpoint" in data:
        out["base_endpoint"] = data["BaseEndpoint"]
    else:
        raise DeserializationError("APIKeyConnectionMetadata.base_endpoint required")
    if "ApiKey" in data:
        out["api_key"] = data["ApiKey"]
    else:
        raise DeserializationError("APIKeyConnectionMetadata.api_key required")
    if "Email" in data:
        out["email"] = data["Email"]
    return out