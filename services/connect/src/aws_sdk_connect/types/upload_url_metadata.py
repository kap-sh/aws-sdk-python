"""Generated from Smithy shape ``com.amazonaws.connect#UploadUrlMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.iso8601_datetime
    import aws_sdk_connect.types.metadata_url
    import aws_sdk_connect.types.url_metadata_signed_headers


class UploadUrlMetadata(TypedDict):
    url: NotRequired["aws_sdk_connect.types.metadata_url.MetadataUrl"]
    """<p>A pre-signed S3 URL that should be used for uploading the attached file. </p>"""
    url_expiry: NotRequired["aws_sdk_connect.types.iso8601_datetime.ISO8601Datetime"]
    """<p>The expiration time of the URL in ISO timestamp. It's specified in ISO 8601 format: <code>yyyy-MM-ddThh:mm:ss.SSSZ</code>. For example, <code>2019-11-08T02:41:28.172Z</code>.</p>"""
    headers_to_include: NotRequired[
        "aws_sdk_connect.types.url_metadata_signed_headers.UrlMetadataSignedHeaders"
    ]
    """<p>A map of headers that should be provided when uploading the attached file. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UploadUrlMetadata) -> dict:
    out: dict = {}
    if "url" in value:
        out["Url"] = value["url"]
    if "url_expiry" in value:
        out["UrlExpiry"] = value["url_expiry"]
    if "headers_to_include" in value:
        import aws_sdk_connect.types.url_metadata_signed_headers

        out["HeadersToInclude"] = (
            aws_sdk_connect.types.url_metadata_signed_headers.serialize_json(
                value["headers_to_include"]
            )
        )
    return out


def deserialize_json(data: dict) -> UploadUrlMetadata:
    out: UploadUrlMetadata = {}  # type: ignore[typeddict-item]
    if "Url" in data:
        out["url"] = data["Url"]
    if "UrlExpiry" in data:
        out["url_expiry"] = data["UrlExpiry"]
    if "HeadersToInclude" in data:
        import aws_sdk_connect.types.url_metadata_signed_headers

        out["headers_to_include"] = (
            aws_sdk_connect.types.url_metadata_signed_headers.deserialize_json(
                data["HeadersToInclude"]
            )
        )
    return out
