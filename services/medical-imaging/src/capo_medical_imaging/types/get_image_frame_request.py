"""Generated from Smithy shape ``com.amazonaws.medicalimaging#GetImageFrameRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_medical_imaging.types.datastore_id
    import capo_medical_imaging.types.image_frame_information
    import capo_medical_imaging.types.image_set_id


class GetImageFrameRequest(TypedDict, closed=True):
    datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    image_set_id: "capo_medical_imaging.types.image_set_id.ImageSetId"
    """<p>The image set identifier.</p>"""
    image_frame_information: (
        "capo_medical_imaging.types.image_frame_information.ImageFrameInformation"
    )
    """<p>Information about the image frame (pixel data) identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImageFrameRequest) -> dict:
    out: dict = {}
    import capo_medical_imaging.types.image_frame_information

    out["imageFrameInformation"] = (
        capo_medical_imaging.types.image_frame_information.serialize_json(
            value["image_frame_information"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetImageFrameRequest:
    out: GetImageFrameRequest = {}  # type: ignore[typeddict-item]
    if "imageFrameInformation" in data:
        import capo_medical_imaging.types.image_frame_information

        out["image_frame_information"] = (
            capo_medical_imaging.types.image_frame_information.deserialize_json(
                data["imageFrameInformation"]
            )
        )
    else:
        raise DeserializationError(
            "GetImageFrameRequest.image_frame_information required"
        )
    return out
