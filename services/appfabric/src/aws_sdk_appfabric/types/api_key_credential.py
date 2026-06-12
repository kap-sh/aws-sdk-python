"""Generated from Smithy shape ``com.amazonaws.appfabric#ApiKeyCredential``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.sensitive_string2048


class ApiKeyCredential(TypedDict):
    api_key: "aws_sdk_appfabric.types.sensitive_string2048.SensitiveString2048"
    """<p>An API key for an application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiKeyCredential) -> dict:
    out: dict = {}
    out["apiKey"] = value["api_key"]
    return out


def deserialize_json(data: dict) -> ApiKeyCredential:
    out: ApiKeyCredential = {}  # type: ignore[typeddict-item]
    if "apiKey" in data:
        out["api_key"] = data["apiKey"]
    else:
        raise DeserializationError("ApiKeyCredential.api_key required")
    return out
