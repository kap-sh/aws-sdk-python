"""Generated from Smithy shape ``com.amazonaws.medicalimaging#DicomJsonMetadataImportConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.dicom_metadata_mappings


class DicomJsonMetadataImportConfiguration(TypedDict):
    dicom_metadata_mappings: (
        "aws_sdk_medical_imaging.types.dicom_metadata_mappings.DicomMetadataMappings"
    )
    """<p>Maps DCM files to their metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DicomJsonMetadataImportConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_medical_imaging.types.dicom_metadata_mappings

    out["dicomMetadataMappings"] = (
        aws_sdk_medical_imaging.types.dicom_metadata_mappings.serialize_json(
            value["dicom_metadata_mappings"]
        )
    )
    return out


def deserialize_json(data: dict) -> DicomJsonMetadataImportConfiguration:
    out: DicomJsonMetadataImportConfiguration = {}  # type: ignore[typeddict-item]
    if "dicomMetadataMappings" in data:
        import aws_sdk_medical_imaging.types.dicom_metadata_mappings

        out["dicom_metadata_mappings"] = (
            aws_sdk_medical_imaging.types.dicom_metadata_mappings.deserialize_json(
                data["dicomMetadataMappings"]
            )
        )
    else:
        raise DeserializationError(
            "DicomJsonMetadataImportConfiguration.dicom_metadata_mappings required"
        )
    return out
