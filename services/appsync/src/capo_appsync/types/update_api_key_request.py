"""Generated from Smithy shape ``com.amazonaws.appsync#UpdateApiKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.long
    import capo_appsync.types.string


class UpdateApiKeyRequest(TypedDict, closed=True):
    api_id: "capo_appsync.types.string.String"
    """<p>The ID for the GraphQL API.</p>"""
    id: "capo_appsync.types.string.String"
    """<p>The API key ID.</p>"""
    description: NotRequired["capo_appsync.types.string.String"]
    """<p>A description of the purpose of the API key.</p>"""
    expires: "capo_appsync.types.long.Long"
    """<p>From the update time, the time after which the API key expires. The date is represented as seconds since the epoch. For more information, see .</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApiKeyRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    out["expires"] = value.get("expires", 0)
    return out


def deserialize_json(data: dict) -> UpdateApiKeyRequest:
    out: UpdateApiKeyRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "expires" in data:
        out["expires"] = data["expires"]
    else:
        out["expires"] = 0
    return out
