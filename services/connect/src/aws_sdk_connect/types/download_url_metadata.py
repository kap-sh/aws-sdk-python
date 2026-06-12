"""Generated from Smithy shape ``com.amazonaws.connect#DownloadUrlMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.iso8601_datetime
    import aws_sdk_connect.types.metadata_url


class DownloadUrlMetadata(TypedDict):
    url: NotRequired["aws_sdk_connect.types.metadata_url.MetadataUrl"]
    """<p>A pre-signed URL that should be used to download the attached file. </p>"""
    url_expiry: NotRequired["aws_sdk_connect.types.iso8601_datetime.ISO8601Datetime"]
    """<p>The expiration time of the URL in ISO timestamp. It's specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DownloadUrlMetadata) -> dict:
    out: dict = {}
    if "url" in value:
        out["Url"] = value["url"]
    if "url_expiry" in value:
        out["UrlExpiry"] = value["url_expiry"]
    return out


def deserialize_json(data: dict) -> DownloadUrlMetadata:
    out: DownloadUrlMetadata = {}  # type: ignore[typeddict-item]
    if "Url" in data:
        out["url"] = data["Url"]
    if "UrlExpiry" in data:
        out["url_expiry"] = data["UrlExpiry"]
    return out
