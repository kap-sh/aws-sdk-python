"""Generated from Smithy shape ``com.amazonaws.appsync#CreateApiKeyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.api_key


class CreateApiKeyResponse(TypedDict):
    api_key: NotRequired["aws_sdk_appsync.types.api_key.ApiKey"]
    """<p>The API key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApiKeyResponse) -> dict:
    out: dict = {}
    if "api_key" in value:
        import aws_sdk_appsync.types.api_key

        out["apiKey"] = aws_sdk_appsync.types.api_key.serialize_json(value["api_key"])
    return out


def deserialize_json(data: dict) -> CreateApiKeyResponse:
    out: CreateApiKeyResponse = {}  # type: ignore[typeddict-item]
    if "apiKey" in data:
        import aws_sdk_appsync.types.api_key

        out["api_key"] = aws_sdk_appsync.types.api_key.deserialize_json(data["apiKey"])
    return out
