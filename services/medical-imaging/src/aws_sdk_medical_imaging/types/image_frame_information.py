"""Generated from Smithy shape ``com.amazonaws.medicalimaging#ImageFrameInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.image_frame_id


class ImageFrameInformation(TypedDict, closed=True):
    image_frame_id: "aws_sdk_medical_imaging.types.image_frame_id.ImageFrameId"
    """<p>The image frame (pixel data) identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageFrameInformation) -> dict:
    out: dict = {}
    out["imageFrameId"] = value["image_frame_id"]
    return out


def deserialize_json(data: dict) -> ImageFrameInformation:
    out: ImageFrameInformation = {}  # type: ignore[typeddict-item]
    if "imageFrameId" in data:
        out["image_frame_id"] = data["imageFrameId"]
    else:
        raise DeserializationError("ImageFrameInformation.image_frame_id required")
    return out
