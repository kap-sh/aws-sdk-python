"""Generated from Smithy shape ``com.amazonaws.quicksight#Image``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.image_source
    import aws_sdk_quicksight.types.string


class Image(TypedDict, closed=True):
    source: NotRequired["aws_sdk_quicksight.types.image_source.ImageSource"]
    """<p>The source of the logo image.</p>"""
    generated_image_url: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The URL that points to the generated logo image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Image) -> dict:
    out: dict = {}
    if "source" in value:
        import aws_sdk_quicksight.types.image_source

        out["Source"] = aws_sdk_quicksight.types.image_source.serialize_json(
            value["source"]
        )
    if "generated_image_url" in value:
        out["GeneratedImageUrl"] = value["generated_image_url"]
    return out


def deserialize_json(data: dict) -> Image:
    out: Image = {}  # type: ignore[typeddict-item]
    if "Source" in data:
        import aws_sdk_quicksight.types.image_source

        out["source"] = aws_sdk_quicksight.types.image_source.deserialize_json(
            data["Source"]
        )
    if "GeneratedImageUrl" in data:
        out["generated_image_url"] = data["GeneratedImageUrl"]
    return out
