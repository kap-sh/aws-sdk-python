"""Generated from Smithy shape ``com.amazonaws.appsync#DeleteApiCacheRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.string


class DeleteApiCacheRequest(TypedDict, closed=True):
    api_id: "capo_appsync.types.string.String"
    """<p>The API ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteApiCacheRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteApiCacheRequest:
    out: DeleteApiCacheRequest = {}  # type: ignore[typeddict-item]
    return out
