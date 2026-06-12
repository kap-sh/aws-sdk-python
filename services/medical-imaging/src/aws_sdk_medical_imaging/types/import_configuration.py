"""Generated from Smithy shape ``com.amazonaws.medicalimaging#ImportConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_medical_imaging.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.dicom_json_metadata_import_configuration


class _ImportConfiguration_dicomJsonMetadataImportConfiguration(TypedDict):
    dicomJsonMetadataImportConfiguration: "aws_sdk_medical_imaging.types.dicom_json_metadata_import_configuration.DicomJsonMetadataImportConfiguration"


ImportConfiguration: TypeAlias = (
    _ImportConfiguration_dicomJsonMetadataImportConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: ImportConfiguration) -> dict:
    if "dicomJsonMetadataImportConfiguration" in value:
        import aws_sdk_medical_imaging.types.dicom_json_metadata_import_configuration

        return {
            "dicomJsonMetadataImportConfiguration": aws_sdk_medical_imaging.types.dicom_json_metadata_import_configuration.serialize_json(
                value["dicomJsonMetadataImportConfiguration"]
            )
        }
    else:
        raise SerializationError("ImportConfiguration: no variant present")


def deserialize_json(data: dict) -> ImportConfiguration:
    if "dicomJsonMetadataImportConfiguration" in data:
        import aws_sdk_medical_imaging.types.dicom_json_metadata_import_configuration

        return {
            "dicomJsonMetadataImportConfiguration": aws_sdk_medical_imaging.types.dicom_json_metadata_import_configuration.deserialize_json(
                data["dicomJsonMetadataImportConfiguration"]
            )
        }
    else:
        raise DeserializationError("ImportConfiguration: no recognized variant key")
