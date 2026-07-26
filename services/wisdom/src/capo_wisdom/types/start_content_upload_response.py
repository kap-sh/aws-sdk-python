"""Generated from Smithy shape ``com.amazonaws.wisdom#StartContentUploadResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_wisdom.types.headers
    import capo_wisdom.types.upload_id
    import capo_wisdom.types.url


class StartContentUploadResponse(TypedDict, closed=True):
    upload_id: "capo_wisdom.types.upload_id.UploadId"
    """<p>The identifier of the upload.</p>"""
    url: "capo_wisdom.types.url.Url"
    """<p>The URL of the upload.</p>"""
    url_expiry: "datetime.datetime"
    """<p>The expiration time of the URL as an epoch timestamp.</p>"""
    headers_to_include: "capo_wisdom.types.headers.Headers"
    """<p>The headers to include in the upload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartContentUploadResponse) -> dict:
    out: dict = {}
    out["uploadId"] = value["upload_id"]
    out["url"] = value["url"]
    import capo_wisdom.types._prelude.timestamp

    out["urlExpiry"] = capo_wisdom.types._prelude.timestamp.serialize_json(
        value["url_expiry"]
    )
    import capo_wisdom.types.headers

    out["headersToInclude"] = capo_wisdom.types.headers.serialize_json(
        value["headers_to_include"]
    )
    return out


def deserialize_json(data: dict) -> StartContentUploadResponse:
    out: StartContentUploadResponse = {}  # type: ignore[typeddict-item]
    if "uploadId" in data:
        out["upload_id"] = data["uploadId"]
    else:
        raise DeserializationError("StartContentUploadResponse.upload_id required")
    if "url" in data:
        out["url"] = data["url"]
    else:
        raise DeserializationError("StartContentUploadResponse.url required")
    if "urlExpiry" in data:
        import capo_wisdom.types._prelude.timestamp

        out["url_expiry"] = capo_wisdom.types._prelude.timestamp.deserialize_json(
            data["urlExpiry"]
        )
    else:
        raise DeserializationError("StartContentUploadResponse.url_expiry required")
    if "headersToInclude" in data:
        import capo_wisdom.types.headers

        out["headers_to_include"] = capo_wisdom.types.headers.deserialize_json(
            data["headersToInclude"]
        )
    else:
        raise DeserializationError(
            "StartContentUploadResponse.headers_to_include required"
        )
    return out
