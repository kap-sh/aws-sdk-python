"""Generated from Smithy shape ``com.amazonaws.quicksight#Image``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.image_source
    import capo_quicksight.types.string


class Image(TypedDict, closed=True):
    source: NotRequired["capo_quicksight.types.image_source.ImageSource"]
    """<p>The source of the logo image.</p>"""
    generated_image_url: NotRequired["capo_quicksight.types.string.String"]
    """<p>The URL that points to the generated logo image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Image) -> dict:
    out: dict = {}
    if "source" in value:
        import capo_quicksight.types.image_source

        out["Source"] = capo_quicksight.types.image_source.serialize_json(
            value["source"]
        )
    if "generated_image_url" in value:
        out["GeneratedImageUrl"] = value["generated_image_url"]
    return out


def deserialize_json(data: dict) -> Image:
    out: Image = {}  # type: ignore[typeddict-item]
    if "Source" in data:
        import capo_quicksight.types.image_source

        out["source"] = capo_quicksight.types.image_source.deserialize_json(
            data["Source"]
        )
    if "GeneratedImageUrl" in data:
        out["generated_image_url"] = data["GeneratedImageUrl"]
    return out
