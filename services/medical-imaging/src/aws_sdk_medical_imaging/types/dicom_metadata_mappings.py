"""Generated from Smithy shape ``com.amazonaws.medicalimaging#DicomMetadataMappings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.dicom_metadata_mapping

DicomMetadataMappings: TypeAlias = list[
    "aws_sdk_medical_imaging.types.dicom_metadata_mapping.DicomMetadataMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: DicomMetadataMappings) -> list:
    import aws_sdk_medical_imaging.types.dicom_metadata_mapping

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medical_imaging.types.dicom_metadata_mapping.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DicomMetadataMappings:
    import aws_sdk_medical_imaging.types.dicom_metadata_mapping

    out: DicomMetadataMappings = []
    for item in data:
        out.append(
            aws_sdk_medical_imaging.types.dicom_metadata_mapping.deserialize_json(item)
        )
    return out
