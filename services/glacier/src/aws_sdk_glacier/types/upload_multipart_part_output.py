"""Generated from Smithy shape ``com.amazonaws.glacier#UploadMultipartPartOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string


class UploadMultipartPartOutput(TypedDict):
    checksum: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The SHA256 tree hash that Amazon Glacier computed for the uploaded part.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UploadMultipartPartOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UploadMultipartPartOutput:
    out: UploadMultipartPartOutput = {}  # type: ignore[typeddict-item]
    return out
