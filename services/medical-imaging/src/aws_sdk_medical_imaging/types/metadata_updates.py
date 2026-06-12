"""Generated from Smithy shape ``com.amazonaws.medicalimaging#MetadataUpdates``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_medical_imaging.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.dicom_updates
    import aws_sdk_medical_imaging.types.image_set_external_version_id


class _MetadataUpdates_DICOMUpdates(TypedDict):
    DICOMUpdates: "aws_sdk_medical_imaging.types.dicom_updates.DICOMUpdates"


class _MetadataUpdates_revertToVersionId(TypedDict):
    revertToVersionId: "aws_sdk_medical_imaging.types.image_set_external_version_id.ImageSetExternalVersionId"


MetadataUpdates: TypeAlias = (
    _MetadataUpdates_DICOMUpdates | _MetadataUpdates_revertToVersionId
)


# --- restJson1 ser/de ---
def serialize_json(value: MetadataUpdates) -> dict:
    if "DICOMUpdates" in value:
        import aws_sdk_medical_imaging.types.dicom_updates

        return {
            "DICOMUpdates": aws_sdk_medical_imaging.types.dicom_updates.serialize_json(
                value["DICOMUpdates"]
            )
        }
    elif "revertToVersionId" in value:
        return {"revertToVersionId": value["revertToVersionId"]}
    else:
        raise SerializationError("MetadataUpdates: no variant present")


def deserialize_json(data: dict) -> MetadataUpdates:
    if "DICOMUpdates" in data:
        import aws_sdk_medical_imaging.types.dicom_updates

        return {
            "DICOMUpdates": aws_sdk_medical_imaging.types.dicom_updates.deserialize_json(
                data["DICOMUpdates"]
            )
        }
    elif "revertToVersionId" in data:
        return {"revertToVersionId": data["revertToVersionId"]}
    else:
        raise DeserializationError("MetadataUpdates: no recognized variant key")
