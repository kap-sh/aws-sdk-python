"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#FilePaths``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gameliftstreams.types.file_path

FilePaths: TypeAlias = list["aws_sdk_gameliftstreams.types.file_path.FilePath"]


# --- restJson1 ser/de ---
def serialize_json(value: FilePaths) -> list:
    return list(value)


def deserialize_json(data: list) -> FilePaths:
    return list(data)
