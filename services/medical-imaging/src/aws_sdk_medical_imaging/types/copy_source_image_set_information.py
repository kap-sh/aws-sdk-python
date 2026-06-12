"""Generated from Smithy shape ``com.amazonaws.medicalimaging#CopySourceImageSetInformation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.image_set_external_version_id
    import aws_sdk_medical_imaging.types.metadata_copies


class CopySourceImageSetInformation(TypedDict):
    latest_version_id: "aws_sdk_medical_imaging.types.image_set_external_version_id.ImageSetExternalVersionId"
    """<p>The latest version identifier for the source image set.</p>"""
    dicom_copies: NotRequired[
        "aws_sdk_medical_imaging.types.metadata_copies.MetadataCopies"
    ]
    """<p>Contains <code>MetadataCopies</code> structure and wraps information related to specific copy use cases. For example, when copying subsets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CopySourceImageSetInformation) -> dict:
    out: dict = {}
    out["latestVersionId"] = value["latest_version_id"]
    if "dicom_copies" in value:
        import aws_sdk_medical_imaging.types.metadata_copies

        out["DICOMCopies"] = (
            aws_sdk_medical_imaging.types.metadata_copies.serialize_json(
                value["dicom_copies"]
            )
        )
    return out


def deserialize_json(data: dict) -> CopySourceImageSetInformation:
    out: CopySourceImageSetInformation = {}  # type: ignore[typeddict-item]
    if "latestVersionId" in data:
        out["latest_version_id"] = data["latestVersionId"]
    else:
        raise DeserializationError(
            "CopySourceImageSetInformation.latest_version_id required"
        )
    if "DICOMCopies" in data:
        import aws_sdk_medical_imaging.types.metadata_copies

        out["dicom_copies"] = (
            aws_sdk_medical_imaging.types.metadata_copies.deserialize_json(
                data["DICOMCopies"]
            )
        )
    return out
