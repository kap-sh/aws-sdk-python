"""Generated from Smithy shape ``com.amazonaws.appsync#ListApiKeysResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.api_keys
    import capo_appsync.types.pagination_token


class ListApiKeysResponse(TypedDict, closed=True):
    api_keys: NotRequired["capo_appsync.types.api_keys.ApiKeys"]
    """<p>The <code>ApiKey</code> objects.</p>"""
    next_token: NotRequired["capo_appsync.types.pagination_token.PaginationToken"]
    """<p>An identifier to pass in the next request to this operation to return the next set of items in the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApiKeysResponse) -> dict:
    out: dict = {}
    if "api_keys" in value:
        import capo_appsync.types.api_keys

        out["apiKeys"] = capo_appsync.types.api_keys.serialize_json(value["api_keys"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListApiKeysResponse:
    out: ListApiKeysResponse = {}  # type: ignore[typeddict-item]
    if "apiKeys" in data:
        import capo_appsync.types.api_keys

        out["api_keys"] = capo_appsync.types.api_keys.deserialize_json(data["apiKeys"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
