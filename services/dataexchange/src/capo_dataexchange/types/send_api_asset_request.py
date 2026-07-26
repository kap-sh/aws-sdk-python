"""Generated from Smithy shape ``com.amazonaws.dataexchange#SendApiAssetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.__string
    import capo_dataexchange.types.map_of__string


class SendApiAssetRequest(TypedDict, closed=True):
    body: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>The request body.</p>"""
    query_string_parameters: NotRequired[
        "capo_dataexchange.types.map_of__string.MapOf__string"
    ]
    """<p>Attach query string parameters to the end of the URI (for example, /v1/examplePath?exampleParam=exampleValue).</p>"""
    asset_id: "capo_dataexchange.types.__string.__string"
    """<p>Asset ID value for the API request.</p>"""
    data_set_id: "capo_dataexchange.types.__string.__string"
    """<p>Data set ID value for the API request.</p>"""
    request_headers: NotRequired["capo_dataexchange.types.map_of__string.MapOf__string"]
    """<p>Any header value prefixed with x-amzn-dataexchange-header- will have that stripped before sending the Asset API request. Use this when you want to override a header that AWS Data Exchange uses. Alternatively, you can use the header without a prefix to the HTTP request.</p>"""
    method: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>HTTP method value for the API request. Alternatively, you can use the appropriate verb in your request.</p>"""
    path: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>URI path value for the API request. Alternatively, you can set the URI path directly by invoking /v1/{pathValue}.</p>"""
    revision_id: "capo_dataexchange.types.__string.__string"
    """<p>Revision ID value for the API request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendApiAssetRequest) -> dict:
    out: dict = {}
    if "body" in value:
        out["Body"] = value["body"]
    return out


def deserialize_json(data: dict) -> SendApiAssetRequest:
    out: SendApiAssetRequest = {}  # type: ignore[typeddict-item]
    if "Body" in data:
        out["body"] = data["Body"]
    return out
