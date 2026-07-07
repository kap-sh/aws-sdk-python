"""Generated from Smithy shape ``com.amazonaws.medicalimaging#ImageSetsMetadataSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.date
    import aws_sdk_medical_imaging.types.dicom_tags
    import aws_sdk_medical_imaging.types.image_set_id
    import aws_sdk_medical_imaging.types.storage_tier


class ImageSetsMetadataSummary(TypedDict, closed=True):
    image_set_id: "aws_sdk_medical_imaging.types.image_set_id.ImageSetId"
    """<p>The image set identifier.</p>"""
    version: NotRequired["int"]
    """<p>The image set version.</p>"""
    created_at: NotRequired["aws_sdk_medical_imaging.types.date.Date"]
    """<p>The time an image set is created. Sample creation date is provided in <code>1985-04-12T23:20:50.52Z</code> format.</p>"""
    updated_at: NotRequired["aws_sdk_medical_imaging.types.date.Date"]
    """<p>The time an image set was last updated.</p>"""
    last_accessed_at: NotRequired["aws_sdk_medical_imaging.types.date.Date"]
    """<p>When the image set was last accessed.</p>"""
    storage_tier: NotRequired["aws_sdk_medical_imaging.types.storage_tier.StorageTier"]
    """<p>The image set's storage tier.</p>"""
    dicom_tags: NotRequired["aws_sdk_medical_imaging.types.dicom_tags.DICOMTags"]
    """<p>The DICOM tags associated with the image set.</p>"""
    is_primary: NotRequired["bool"]
    """<p>The flag to determine whether the image set is primary or not.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageSetsMetadataSummary) -> dict:
    out: dict = {}
    out["imageSetId"] = value["image_set_id"]
    if "version" in value:
        out["version"] = value["version"]
    if "created_at" in value:
        import aws_sdk_medical_imaging.types.date

        out["createdAt"] = aws_sdk_medical_imaging.types.date.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_medical_imaging.types.date

        out["updatedAt"] = aws_sdk_medical_imaging.types.date.serialize_json(
            value["updated_at"]
        )
    if "last_accessed_at" in value:
        import aws_sdk_medical_imaging.types.date

        out["lastAccessedAt"] = aws_sdk_medical_imaging.types.date.serialize_json(
            value["last_accessed_at"]
        )
    if "storage_tier" in value:
        import aws_sdk_medical_imaging.types.storage_tier

        out["storageTier"] = aws_sdk_medical_imaging.types.storage_tier.serialize_json(
            value["storage_tier"]
        )
    if "dicom_tags" in value:
        import aws_sdk_medical_imaging.types.dicom_tags

        out["DICOMTags"] = aws_sdk_medical_imaging.types.dicom_tags.serialize_json(
            value["dicom_tags"]
        )
    if "is_primary" in value:
        out["isPrimary"] = value["is_primary"]
    return out


def deserialize_json(data: dict) -> ImageSetsMetadataSummary:
    out: ImageSetsMetadataSummary = {}  # type: ignore[typeddict-item]
    if "imageSetId" in data:
        out["image_set_id"] = data["imageSetId"]
    else:
        raise DeserializationError("ImageSetsMetadataSummary.image_set_id required")
    if "version" in data:
        out["version"] = data["version"]
    if "createdAt" in data:
        import aws_sdk_medical_imaging.types.date

        out["created_at"] = aws_sdk_medical_imaging.types.date.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_medical_imaging.types.date

        out["updated_at"] = aws_sdk_medical_imaging.types.date.deserialize_json(
            data["updatedAt"]
        )
    if "lastAccessedAt" in data:
        import aws_sdk_medical_imaging.types.date

        out["last_accessed_at"] = aws_sdk_medical_imaging.types.date.deserialize_json(
            data["lastAccessedAt"]
        )
    if "storageTier" in data:
        import aws_sdk_medical_imaging.types.storage_tier

        out["storage_tier"] = (
            aws_sdk_medical_imaging.types.storage_tier.deserialize_json(
                data["storageTier"]
            )
        )
    if "DICOMTags" in data:
        import aws_sdk_medical_imaging.types.dicom_tags

        out["dicom_tags"] = aws_sdk_medical_imaging.types.dicom_tags.deserialize_json(
            data["DICOMTags"]
        )
    if "isPrimary" in data:
        out["is_primary"] = data["isPrimary"]
    return out
