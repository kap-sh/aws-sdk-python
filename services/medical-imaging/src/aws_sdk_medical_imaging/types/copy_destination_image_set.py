"""Generated from Smithy shape ``com.amazonaws.medicalimaging#CopyDestinationImageSet``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.image_set_external_version_id
    import aws_sdk_medical_imaging.types.image_set_id


class CopyDestinationImageSet(TypedDict, closed=True):
    image_set_id: "aws_sdk_medical_imaging.types.image_set_id.ImageSetId"
    """<p>The image set identifier for the destination image set.</p>"""
    latest_version_id: "aws_sdk_medical_imaging.types.image_set_external_version_id.ImageSetExternalVersionId"
    """<p>The latest version identifier for the destination image set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CopyDestinationImageSet) -> dict:
    out: dict = {}
    out["imageSetId"] = value["image_set_id"]
    out["latestVersionId"] = value["latest_version_id"]
    return out


def deserialize_json(data: dict) -> CopyDestinationImageSet:
    out: CopyDestinationImageSet = {}  # type: ignore[typeddict-item]
    if "imageSetId" in data:
        out["image_set_id"] = data["imageSetId"]
    else:
        raise DeserializationError("CopyDestinationImageSet.image_set_id required")
    if "latestVersionId" in data:
        out["latest_version_id"] = data["latestVersionId"]
    else:
        raise DeserializationError("CopyDestinationImageSet.latest_version_id required")
    return out
