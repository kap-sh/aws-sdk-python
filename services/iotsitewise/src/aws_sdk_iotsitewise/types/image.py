"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Image``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.image_file


class Image(TypedDict, closed=True):
    id: NotRequired["aws_sdk_iotsitewise.types.id.ID"]
    """<p>The ID of an existing image. Specify this parameter to keep an existing image.</p>"""
    file: NotRequired["aws_sdk_iotsitewise.types.image_file.ImageFile"]


# --- restJson1 ser/de ---
def serialize_json(value: Image) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "file" in value:
        import aws_sdk_iotsitewise.types.image_file

        out["file"] = aws_sdk_iotsitewise.types.image_file.serialize_json(value["file"])
    return out


def deserialize_json(data: dict) -> Image:
    out: Image = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "file" in data:
        import aws_sdk_iotsitewise.types.image_file

        out["file"] = aws_sdk_iotsitewise.types.image_file.deserialize_json(
            data["file"]
        )
    return out
