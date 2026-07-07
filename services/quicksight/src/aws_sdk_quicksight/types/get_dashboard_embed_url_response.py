"""Generated from Smithy shape ``com.amazonaws.quicksight#GetDashboardEmbedUrlResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.embedding_url
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class GetDashboardEmbedUrlResponse(TypedDict, closed=True):
    embed_url: NotRequired["aws_sdk_quicksight.types.embedding_url.EmbeddingUrl"]
    """<p>A single-use URL that you can put into your server-side webpage to embed your dashboard. This URL is valid for 5 minutes. The API operation provides the URL with an <code>auth_code</code> value that enables one (and only one) sign-on to a user session that is valid for 10 hours. </p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDashboardEmbedUrlResponse) -> dict:
    out: dict = {}
    if "embed_url" in value:
        out["EmbedUrl"] = value["embed_url"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> GetDashboardEmbedUrlResponse:
    out: GetDashboardEmbedUrlResponse = {}  # type: ignore[typeddict-item]
    if "EmbedUrl" in data:
        out["embed_url"] = data["EmbedUrl"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
