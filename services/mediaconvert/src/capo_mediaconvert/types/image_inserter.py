"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ImageInserter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min100_max1000
    import capo_mediaconvert.types.__list_of_insertable_image


class ImageInserter(TypedDict, closed=True):
    insertable_images: NotRequired[
        "capo_mediaconvert.types.__list_of_insertable_image.__listOfInsertableImage"
    ]
    """Specify the images that you want to overlay on your video. The images must be PNG or TGA files."""
    sdr_reference_white_level: NotRequired[
        "capo_mediaconvert.types.__integer_min100_max1000.__integerMin100Max1000"
    ]
    """Specify the reference white level, in nits, for all of your image inserter images. Use to correct brightness levels within HDR10 outputs. For 1,000 nit peak brightness displays, we recommend that you set SDR reference white level to 203 (according to ITU-R BT.2408). Leave blank to use the default value of 100, or specify an integer from 100 to 1000."""


# --- restJson1 ser/de ---
def serialize_json(value: ImageInserter) -> dict:
    out: dict = {}
    if "insertable_images" in value:
        import capo_mediaconvert.types.__list_of_insertable_image

        out["insertableImages"] = (
            capo_mediaconvert.types.__list_of_insertable_image.serialize_json(
                value["insertable_images"]
            )
        )
    if "sdr_reference_white_level" in value:
        out["sdrReferenceWhiteLevel"] = value["sdr_reference_white_level"]
    return out


def deserialize_json(data: dict) -> ImageInserter:
    out: ImageInserter = {}  # type: ignore[typeddict-item]
    if "insertableImages" in data:
        import capo_mediaconvert.types.__list_of_insertable_image

        out["insertable_images"] = (
            capo_mediaconvert.types.__list_of_insertable_image.deserialize_json(
                data["insertableImages"]
            )
        )
    if "sdrReferenceWhiteLevel" in data:
        out["sdr_reference_white_level"] = data["sdrReferenceWhiteLevel"]
    return out
