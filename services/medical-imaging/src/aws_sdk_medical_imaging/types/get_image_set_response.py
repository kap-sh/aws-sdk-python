"""Generated from Smithy shape ``com.amazonaws.medicalimaging#GetImageSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.arn
    import aws_sdk_medical_imaging.types.datastore_id
    import aws_sdk_medical_imaging.types.date
    import aws_sdk_medical_imaging.types.image_set_external_version_id
    import aws_sdk_medical_imaging.types.image_set_id
    import aws_sdk_medical_imaging.types.image_set_state
    import aws_sdk_medical_imaging.types.image_set_workflow_status
    import aws_sdk_medical_imaging.types.message
    import aws_sdk_medical_imaging.types.overrides
    import aws_sdk_medical_imaging.types.storage_tier


class GetImageSetResponse(TypedDict, closed=True):
    datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    image_set_id: "aws_sdk_medical_imaging.types.image_set_id.ImageSetId"
    """<p>The image set identifier.</p>"""
    version_id: "aws_sdk_medical_imaging.types.image_set_external_version_id.ImageSetExternalVersionId"
    """<p>The image set version identifier.</p>"""
    image_set_state: "aws_sdk_medical_imaging.types.image_set_state.ImageSetState"
    """<p>The image set state.</p>"""
    image_set_workflow_status: NotRequired[
        "aws_sdk_medical_imaging.types.image_set_workflow_status.ImageSetWorkflowStatus"
    ]
    """<p>The image set workflow status.</p>"""
    created_at: NotRequired["aws_sdk_medical_imaging.types.date.Date"]
    """<p>The timestamp when image set properties were created.</p>"""
    updated_at: NotRequired["aws_sdk_medical_imaging.types.date.Date"]
    """<p>The timestamp when image set properties were updated.</p>"""
    deleted_at: NotRequired["aws_sdk_medical_imaging.types.date.Date"]
    """<p>The timestamp when the image set properties were deleted.</p>"""
    message: NotRequired["aws_sdk_medical_imaging.types.message.Message"]
    """<p>The error message thrown if an image set action fails.</p>"""
    image_set_arn: NotRequired["aws_sdk_medical_imaging.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) assigned to the image set.</p>"""
    overrides: NotRequired["aws_sdk_medical_imaging.types.overrides.Overrides"]
    """<p>This object contains the details of any overrides used while creating a specific image set version. If an image set was copied or updated using the <code>force</code> flag, this object will contain the <code>forced</code> flag.</p>"""
    is_primary: NotRequired["bool"]
    """<p>The flag to determine whether the image set is primary or not.</p>"""
    last_accessed_at: NotRequired["aws_sdk_medical_imaging.types.date.Date"]
    """<p>When the image set was last accessed.</p>"""
    storage_tier: NotRequired["aws_sdk_medical_imaging.types.storage_tier.StorageTier"]
    """<p>The storage tier of the image set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImageSetResponse) -> dict:
    out: dict = {}
    out["datastoreId"] = value["datastore_id"]
    out["imageSetId"] = value["image_set_id"]
    out["versionId"] = value["version_id"]
    import aws_sdk_medical_imaging.types.image_set_state

    out["imageSetState"] = aws_sdk_medical_imaging.types.image_set_state.serialize_json(
        value["image_set_state"]
    )
    if "image_set_workflow_status" in value:
        import aws_sdk_medical_imaging.types.image_set_workflow_status

        out["imageSetWorkflowStatus"] = (
            aws_sdk_medical_imaging.types.image_set_workflow_status.serialize_json(
                value["image_set_workflow_status"]
            )
        )
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
    if "deleted_at" in value:
        import aws_sdk_medical_imaging.types.date

        out["deletedAt"] = aws_sdk_medical_imaging.types.date.serialize_json(
            value["deleted_at"]
        )
    if "message" in value:
        out["message"] = value["message"]
    if "image_set_arn" in value:
        out["imageSetArn"] = value["image_set_arn"]
    if "overrides" in value:
        import aws_sdk_medical_imaging.types.overrides

        out["overrides"] = aws_sdk_medical_imaging.types.overrides.serialize_json(
            value["overrides"]
        )
    if "is_primary" in value:
        out["isPrimary"] = value["is_primary"]
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
    return out


def deserialize_json(data: dict) -> GetImageSetResponse:
    out: GetImageSetResponse = {}  # type: ignore[typeddict-item]
    if "datastoreId" in data:
        out["datastore_id"] = data["datastoreId"]
    else:
        raise DeserializationError("GetImageSetResponse.datastore_id required")
    if "imageSetId" in data:
        out["image_set_id"] = data["imageSetId"]
    else:
        raise DeserializationError("GetImageSetResponse.image_set_id required")
    if "versionId" in data:
        out["version_id"] = data["versionId"]
    else:
        raise DeserializationError("GetImageSetResponse.version_id required")
    if "imageSetState" in data:
        import aws_sdk_medical_imaging.types.image_set_state

        out["image_set_state"] = (
            aws_sdk_medical_imaging.types.image_set_state.deserialize_json(
                data["imageSetState"]
            )
        )
    else:
        raise DeserializationError("GetImageSetResponse.image_set_state required")
    if "imageSetWorkflowStatus" in data:
        import aws_sdk_medical_imaging.types.image_set_workflow_status

        out["image_set_workflow_status"] = (
            aws_sdk_medical_imaging.types.image_set_workflow_status.deserialize_json(
                data["imageSetWorkflowStatus"]
            )
        )
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
    if "deletedAt" in data:
        import aws_sdk_medical_imaging.types.date

        out["deleted_at"] = aws_sdk_medical_imaging.types.date.deserialize_json(
            data["deletedAt"]
        )
    if "message" in data:
        out["message"] = data["message"]
    if "imageSetArn" in data:
        out["image_set_arn"] = data["imageSetArn"]
    if "overrides" in data:
        import aws_sdk_medical_imaging.types.overrides

        out["overrides"] = aws_sdk_medical_imaging.types.overrides.deserialize_json(
            data["overrides"]
        )
    if "isPrimary" in data:
        out["is_primary"] = data["isPrimary"]
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
    return out
