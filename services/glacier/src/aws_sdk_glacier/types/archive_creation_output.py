"""Generated from Smithy shape ``com.amazonaws.glacier#ArchiveCreationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string


class ArchiveCreationOutput(TypedDict):
    location: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The relative URI path of the newly added archive resource.</p>"""
    checksum: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The checksum of the archive computed by Amazon Glacier.</p>"""
    archive_id: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The ID of the archive. This value is also included as part of the location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArchiveCreationOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ArchiveCreationOutput:
    out: ArchiveCreationOutput = {}  # type: ignore[typeddict-item]
    return out
