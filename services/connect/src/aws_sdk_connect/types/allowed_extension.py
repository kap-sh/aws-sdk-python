"""Generated from Smithy shape ``com.amazonaws.connect#AllowedExtension``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.file_extension


class AllowedExtension(TypedDict):
    extension: "aws_sdk_connect.types.file_extension.FileExtension"
    """<p>The file extension. The extension must be between 1 and 10 characters and can contain only alphanumeric characters, hyphens, and underscores.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AllowedExtension) -> dict:
    out: dict = {}
    out["Extension"] = value["extension"]
    return out


def deserialize_json(data: dict) -> AllowedExtension:
    out: AllowedExtension = {}  # type: ignore[typeddict-item]
    if "Extension" in data:
        out["extension"] = data["Extension"]
    else:
        raise DeserializationError("AllowedExtension.extension required")
    return out
