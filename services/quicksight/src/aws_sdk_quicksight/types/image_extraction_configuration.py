"""Generated from Smithy shape ``com.amazonaws.quicksight#ImageExtractionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.image_extraction_status


class ImageExtractionConfiguration(TypedDict):
    image_extraction_status: (
        "aws_sdk_quicksight.types.image_extraction_status.ImageExtractionStatus"
    )
    """<p>The status of image extraction. Valid values are ENABLED and DISABLED.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageExtractionConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.image_extraction_status

    out["imageExtractionStatus"] = (
        aws_sdk_quicksight.types.image_extraction_status.serialize_json(
            value["image_extraction_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> ImageExtractionConfiguration:
    out: ImageExtractionConfiguration = {}  # type: ignore[typeddict-item]
    if "imageExtractionStatus" in data:
        import aws_sdk_quicksight.types.image_extraction_status

        out["image_extraction_status"] = (
            aws_sdk_quicksight.types.image_extraction_status.deserialize_json(
                data["imageExtractionStatus"]
            )
        )
    else:
        raise DeserializationError(
            "ImageExtractionConfiguration.image_extraction_status required"
        )
    return out
