"""Generated from Smithy shape ``com.amazonaws.medicalimaging#MetadataUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_medical_imaging.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_medical_imaging.types.dicom_updates
    import capo_medical_imaging.types.image_set_external_version_id


class _MetadataUpdates_DICOMUpdates(TypedDict, closed=True):
    DICOMUpdates: "capo_medical_imaging.types.dicom_updates.DICOMUpdates"


class _MetadataUpdates_revertToVersionId(TypedDict, closed=True):
    revertToVersionId: "capo_medical_imaging.types.image_set_external_version_id.ImageSetExternalVersionId"


MetadataUpdates: TypeAlias = (
    _MetadataUpdates_DICOMUpdates | _MetadataUpdates_revertToVersionId
)


# --- restJson1 ser/de ---
def serialize_json(value: MetadataUpdates) -> dict:
    if "DICOMUpdates" in value:
        import capo_medical_imaging.types.dicom_updates

        return {
            "DICOMUpdates": capo_medical_imaging.types.dicom_updates.serialize_json(
                value["DICOMUpdates"]
            )
        }
    elif "revertToVersionId" in value:
        return {"revertToVersionId": value["revertToVersionId"]}
    else:
        raise SerializationError("MetadataUpdates: no variant present")


def deserialize_json(data: dict) -> MetadataUpdates:
    if "DICOMUpdates" in data:
        import capo_medical_imaging.types.dicom_updates

        return {
            "DICOMUpdates": capo_medical_imaging.types.dicom_updates.deserialize_json(
                data["DICOMUpdates"]
            )
        }
    elif "revertToVersionId" in data:
        return {"revertToVersionId": data["revertToVersionId"]}
    else:
        raise DeserializationError("MetadataUpdates: no recognized variant key")
