"""Generated from Smithy shape ``com.amazonaws.apigateway#ExportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.blob
    import capo_api_gateway.types.string


class ExportResponse(TypedDict, closed=True):
    content_type: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The content-type header value in the HTTP response. This will correspond to a valid 'accept' type in the request.</p>"""
    content_disposition: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The content-disposition header value in the HTTP response.</p>"""
    body: NotRequired["capo_api_gateway.types.blob.Blob"]
    """<p>The binary blob response to GetExport, which contains the export.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportResponse) -> dict:
    out: dict = {}
    if "body" in value:
        import capo_api_gateway.types.blob

        out["body"] = capo_api_gateway.types.blob.serialize_json(value["body"])
    return out


def deserialize_json(data: dict) -> ExportResponse:
    out: ExportResponse = {}  # type: ignore[typeddict-item]
    if "body" in data:
        import capo_api_gateway.types.blob

        out["body"] = capo_api_gateway.types.blob.deserialize_json(data["body"])
    return out
