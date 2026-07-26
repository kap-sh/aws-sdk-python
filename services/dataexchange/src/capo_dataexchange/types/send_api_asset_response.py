"""Generated from Smithy shape ``com.amazonaws.dataexchange#SendApiAssetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.__string
    import capo_dataexchange.types.map_of__string


class SendApiAssetResponse(TypedDict, closed=True):
    body: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>The response body from the underlying API tracked by the API asset.</p>"""
    response_headers: NotRequired[
        "capo_dataexchange.types.map_of__string.MapOf__string"
    ]
    """<p>The response headers from the underlying API tracked by the API asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendApiAssetResponse) -> dict:
    out: dict = {}
    if "body" in value:
        out["Body"] = value["body"]
    return out


def deserialize_json(data: dict) -> SendApiAssetResponse:
    out: SendApiAssetResponse = {}  # type: ignore[typeddict-item]
    if "Body" in data:
        out["body"] = data["Body"]
    return out
