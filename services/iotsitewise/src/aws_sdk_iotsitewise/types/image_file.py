"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ImageFile``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.image_file_data
    import aws_sdk_iotsitewise.types.image_file_type


class ImageFile(TypedDict):
    data: "aws_sdk_iotsitewise.types.image_file_data.ImageFileData"
    """<p>The image file contents, represented as a base64-encoded string. The file size must be less than 1 MB.</p>"""
    type: "aws_sdk_iotsitewise.types.image_file_type.ImageFileType"
    """<p>The file type of the image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageFile) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.image_file_data

    out["data"] = aws_sdk_iotsitewise.types.image_file_data.serialize_json(
        value["data"]
    )
    import aws_sdk_iotsitewise.types.image_file_type

    out["type"] = aws_sdk_iotsitewise.types.image_file_type.serialize_json(
        value["type"]
    )
    return out


def deserialize_json(data: dict) -> ImageFile:
    out: ImageFile = {}  # type: ignore[typeddict-item]
    if "data" in data:
        import aws_sdk_iotsitewise.types.image_file_data

        out["data"] = aws_sdk_iotsitewise.types.image_file_data.deserialize_json(
            data["data"]
        )
    else:
        raise DeserializationError("ImageFile.data required")
    if "type" in data:
        import aws_sdk_iotsitewise.types.image_file_type

        out["type"] = aws_sdk_iotsitewise.types.image_file_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("ImageFile.type required")
    return out
