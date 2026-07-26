"""Generated from Smithy shape ``com.amazonaws.quicksight#ImageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.image_source


class ImageConfiguration(TypedDict, closed=True):
    source: NotRequired["capo_quicksight.types.image_source.ImageSource"]
    """<p>The source of the image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageConfiguration) -> dict:
    out: dict = {}
    if "source" in value:
        import capo_quicksight.types.image_source

        out["Source"] = capo_quicksight.types.image_source.serialize_json(
            value["source"]
        )
    return out


def deserialize_json(data: dict) -> ImageConfiguration:
    out: ImageConfiguration = {}  # type: ignore[typeddict-item]
    if "Source" in data:
        import capo_quicksight.types.image_source

        out["source"] = capo_quicksight.types.image_source.deserialize_json(
            data["Source"]
        )
    return out
