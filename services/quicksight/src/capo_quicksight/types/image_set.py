"""Generated from Smithy shape ``com.amazonaws.quicksight#ImageSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.image


class ImageSet(TypedDict, closed=True):
    original: "capo_quicksight.types.image.Image"
    """<p>The original image.</p>"""
    height64: NotRequired["capo_quicksight.types.image.Image"]
    """<p>The image with the height set to 64 pixels.</p>"""
    height32: NotRequired["capo_quicksight.types.image.Image"]
    """<p>The image with the height set to 32 pixels.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageSet) -> dict:
    out: dict = {}
    import capo_quicksight.types.image

    out["Original"] = capo_quicksight.types.image.serialize_json(value["original"])
    if "height64" in value:
        import capo_quicksight.types.image

        out["Height64"] = capo_quicksight.types.image.serialize_json(value["height64"])
    if "height32" in value:
        import capo_quicksight.types.image

        out["Height32"] = capo_quicksight.types.image.serialize_json(value["height32"])
    return out


def deserialize_json(data: dict) -> ImageSet:
    out: ImageSet = {}  # type: ignore[typeddict-item]
    if "Original" in data:
        import capo_quicksight.types.image

        out["original"] = capo_quicksight.types.image.deserialize_json(data["Original"])
    else:
        raise DeserializationError("ImageSet.original required")
    if "Height64" in data:
        import capo_quicksight.types.image

        out["height64"] = capo_quicksight.types.image.deserialize_json(data["Height64"])
    if "Height32" in data:
        import capo_quicksight.types.image

        out["height32"] = capo_quicksight.types.image.deserialize_json(data["Height32"])
    return out
