"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetImageSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.sheet_image_static_file_source


class SheetImageSource(TypedDict, closed=True):
    sheet_image_static_file_source: NotRequired[
        "aws_sdk_quicksight.types.sheet_image_static_file_source.SheetImageStaticFileSource"
    ]
    """<p>The source of the static file that contains the image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetImageSource) -> dict:
    out: dict = {}
    if "sheet_image_static_file_source" in value:
        import aws_sdk_quicksight.types.sheet_image_static_file_source

        out["SheetImageStaticFileSource"] = (
            aws_sdk_quicksight.types.sheet_image_static_file_source.serialize_json(
                value["sheet_image_static_file_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> SheetImageSource:
    out: SheetImageSource = {}  # type: ignore[typeddict-item]
    if "SheetImageStaticFileSource" in data:
        import aws_sdk_quicksight.types.sheet_image_static_file_source

        out["sheet_image_static_file_source"] = (
            aws_sdk_quicksight.types.sheet_image_static_file_source.deserialize_json(
                data["SheetImageStaticFileSource"]
            )
        )
    return out
