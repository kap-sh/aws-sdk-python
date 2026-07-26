"""Generated from Smithy shape ``com.amazonaws.s3files#GetSynchronizationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3files.types.file_system_id


class GetSynchronizationConfigurationRequest(TypedDict, closed=True):
    file_system_id: "capo_s3files.types.file_system_id.FileSystemId"
    """<p>The ID or Amazon Resource Name (ARN) of the S3 File System to retrieve the synchronization configuration for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSynchronizationConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSynchronizationConfigurationRequest:
    out: GetSynchronizationConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
