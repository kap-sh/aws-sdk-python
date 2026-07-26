"""Generated from Smithy shape ``com.amazonaws.medicalimaging#CopyImageSetInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_medical_imaging.types.copy_destination_image_set
    import capo_medical_imaging.types.copy_source_image_set_information


class CopyImageSetInformation(TypedDict, closed=True):
    source_image_set: "capo_medical_imaging.types.copy_source_image_set_information.CopySourceImageSetInformation"
    """<p>The source image set.</p>"""
    destination_image_set: NotRequired[
        "capo_medical_imaging.types.copy_destination_image_set.CopyDestinationImageSet"
    ]
    """<p>The destination image set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CopyImageSetInformation) -> dict:
    out: dict = {}
    import capo_medical_imaging.types.copy_source_image_set_information

    out["sourceImageSet"] = (
        capo_medical_imaging.types.copy_source_image_set_information.serialize_json(
            value["source_image_set"]
        )
    )
    if "destination_image_set" in value:
        import capo_medical_imaging.types.copy_destination_image_set

        out["destinationImageSet"] = (
            capo_medical_imaging.types.copy_destination_image_set.serialize_json(
                value["destination_image_set"]
            )
        )
    return out


def deserialize_json(data: dict) -> CopyImageSetInformation:
    out: CopyImageSetInformation = {}  # type: ignore[typeddict-item]
    if "sourceImageSet" in data:
        import capo_medical_imaging.types.copy_source_image_set_information

        out["source_image_set"] = (
            capo_medical_imaging.types.copy_source_image_set_information.deserialize_json(
                data["sourceImageSet"]
            )
        )
    else:
        raise DeserializationError("CopyImageSetInformation.source_image_set required")
    if "destinationImageSet" in data:
        import capo_medical_imaging.types.copy_destination_image_set

        out["destination_image_set"] = (
            capo_medical_imaging.types.copy_destination_image_set.deserialize_json(
                data["destinationImageSet"]
            )
        )
    return out
