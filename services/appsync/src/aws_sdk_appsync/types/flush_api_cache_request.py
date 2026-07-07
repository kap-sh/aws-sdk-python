"""Generated from Smithy shape ``com.amazonaws.appsync#FlushApiCacheRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.string


class FlushApiCacheRequest(TypedDict, closed=True):
    api_id: "aws_sdk_appsync.types.string.String"
    """<p>The API ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlushApiCacheRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> FlushApiCacheRequest:
    out: FlushApiCacheRequest = {}  # type: ignore[typeddict-item]
    return out
