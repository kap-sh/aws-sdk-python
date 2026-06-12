"""Generated from Smithy shape ``com.amazonaws.appsync#CreateApiKeyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.long
    import aws_sdk_appsync.types.string


class CreateApiKeyRequest(TypedDict):
    api_id: "aws_sdk_appsync.types.string.String"
    """<p>The ID for your GraphQL API.</p>"""
    description: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>A description of the purpose of the API key.</p>"""
    expires: "aws_sdk_appsync.types.long.Long"
    """<p>From the creation time, the time after which the API key expires. The date is represented as seconds since the epoch, rounded down to the nearest hour. The default value for this parameter is 7 days from creation time. For more information, see .</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApiKeyRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    out["expires"] = value.get("expires", 0)
    return out


def deserialize_json(data: dict) -> CreateApiKeyRequest:
    out: CreateApiKeyRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "expires" in data:
        out["expires"] = data["expires"]
    else:
        out["expires"] = 0
    return out
