"""Generated from Smithy shape ``com.amazonaws.workdocs#UploadMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.signed_header_map
    import aws_sdk_workdocs.types.url_type


class UploadMetadata(TypedDict, closed=True):
    upload_url: NotRequired["aws_sdk_workdocs.types.url_type.UrlType"]
    """<p>The URL of the upload.</p>"""
    signed_headers: NotRequired[
        "aws_sdk_workdocs.types.signed_header_map.SignedHeaderMap"
    ]
    """<p>The signed headers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UploadMetadata) -> dict:
    out: dict = {}
    if "upload_url" in value:
        out["UploadUrl"] = value["upload_url"]
    if "signed_headers" in value:
        import aws_sdk_workdocs.types.signed_header_map

        out["SignedHeaders"] = aws_sdk_workdocs.types.signed_header_map.serialize_json(
            value["signed_headers"]
        )
    return out


def deserialize_json(data: dict) -> UploadMetadata:
    out: UploadMetadata = {}  # type: ignore[typeddict-item]
    if "UploadUrl" in data:
        out["upload_url"] = data["UploadUrl"]
    if "SignedHeaders" in data:
        import aws_sdk_workdocs.types.signed_header_map

        out["signed_headers"] = (
            aws_sdk_workdocs.types.signed_header_map.deserialize_json(
                data["SignedHeaders"]
            )
        )
    return out
