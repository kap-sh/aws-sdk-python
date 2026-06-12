"""Generated from Smithy shape ``com.amazonaws.glacier#InitiateMultipartUploadOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string


class InitiateMultipartUploadOutput(TypedDict):
    location: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The relative URI path of the multipart upload ID Amazon Glacier created.</p>"""
    upload_id: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The ID of the multipart upload. This value is also included as part of the location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InitiateMultipartUploadOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> InitiateMultipartUploadOutput:
    out: InitiateMultipartUploadOutput = {}  # type: ignore[typeddict-item]
    return out
