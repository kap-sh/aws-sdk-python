"""Generated from Smithy shape ``com.amazonaws.m2#EfsStorageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.string200


class EfsStorageConfiguration(TypedDict, closed=True):
    file_system_id: "aws_sdk_m2.types.string200.String200"
    """<p>The file system identifier.</p>"""
    mount_point: "aws_sdk_m2.types.string200.String200"
    """<p>The mount point for the file system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EfsStorageConfiguration) -> dict:
    out: dict = {}
    out["file-system-id"] = value["file_system_id"]
    out["mount-point"] = value["mount_point"]
    return out


def deserialize_json(data: dict) -> EfsStorageConfiguration:
    out: EfsStorageConfiguration = {}  # type: ignore[typeddict-item]
    if "file-system-id" in data:
        out["file_system_id"] = data["file-system-id"]
    else:
        raise DeserializationError("EfsStorageConfiguration.file_system_id required")
    if "mount-point" in data:
        out["mount_point"] = data["mount-point"]
    else:
        raise DeserializationError("EfsStorageConfiguration.mount_point required")
    return out
