"""Generated from Smithy shape ``com.amazonaws.quicksight#ImageStaticFile``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.static_file_source


class ImageStaticFile(TypedDict):
    static_file_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID of the static file that contains an image.</p>"""
    source: NotRequired["aws_sdk_quicksight.types.static_file_source.StaticFileSource"]
    """<p>The source of the image static file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageStaticFile) -> dict:
    out: dict = {}
    out["StaticFileId"] = value["static_file_id"]
    if "source" in value:
        import aws_sdk_quicksight.types.static_file_source

        out["Source"] = aws_sdk_quicksight.types.static_file_source.serialize_json(
            value["source"]
        )
    return out


def deserialize_json(data: dict) -> ImageStaticFile:
    out: ImageStaticFile = {}  # type: ignore[typeddict-item]
    if "StaticFileId" in data:
        out["static_file_id"] = data["StaticFileId"]
    else:
        raise DeserializationError("ImageStaticFile.static_file_id required")
    if "Source" in data:
        import aws_sdk_quicksight.types.static_file_source

        out["source"] = aws_sdk_quicksight.types.static_file_source.deserialize_json(
            data["Source"]
        )
    return out
