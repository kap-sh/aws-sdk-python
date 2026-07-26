"""Generated from Smithy shape ``com.amazonaws.quicksight#ImageSetConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.image_configuration


class ImageSetConfiguration(TypedDict, closed=True):
    original: "capo_quicksight.types.image_configuration.ImageConfiguration"
    """<p>The original image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageSetConfiguration) -> dict:
    out: dict = {}
    import capo_quicksight.types.image_configuration

    out["Original"] = capo_quicksight.types.image_configuration.serialize_json(
        value["original"]
    )
    return out


def deserialize_json(data: dict) -> ImageSetConfiguration:
    out: ImageSetConfiguration = {}  # type: ignore[typeddict-item]
    if "Original" in data:
        import capo_quicksight.types.image_configuration

        out["original"] = capo_quicksight.types.image_configuration.deserialize_json(
            data["Original"]
        )
    else:
        raise DeserializationError("ImageSetConfiguration.original required")
    return out
