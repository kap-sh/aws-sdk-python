"""Generated from Smithy shape ``com.amazonaws.deadline#FileSystemLocation``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.file_system_location_name
    import aws_sdk_deadline.types.file_system_location_type
    import aws_sdk_deadline.types.path_string


class FileSystemLocation(TypedDict):
    name: "aws_sdk_deadline.types.file_system_location_name.FileSystemLocationName"
    """<p>The location name.</p>"""
    path: "aws_sdk_deadline.types.path_string.PathString"
    """<p>The file path.</p>"""
    type: "aws_sdk_deadline.types.file_system_location_type.FileSystemLocationType"
    """<p>The type of file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileSystemLocation) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["path"] = value["path"]
    import aws_sdk_deadline.types.file_system_location_type

    out["type"] = aws_sdk_deadline.types.file_system_location_type.serialize_json(
        value["type"]
    )
    return out


def deserialize_json(data: dict) -> FileSystemLocation:
    out: FileSystemLocation = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("FileSystemLocation.name required")
    if "path" in data:
        out["path"] = data["path"]
    else:
        raise DeserializationError("FileSystemLocation.path required")
    if "type" in data:
        import aws_sdk_deadline.types.file_system_location_type

        out["type"] = aws_sdk_deadline.types.file_system_location_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("FileSystemLocation.type required")
    return out
