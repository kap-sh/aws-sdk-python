"""Generated from Smithy shape ``com.amazonaws.medicalimaging#ImageSetProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.date
    import aws_sdk_medical_imaging.types.image_set_external_version_id
    import aws_sdk_medical_imaging.types.image_set_id
    import aws_sdk_medical_imaging.types.image_set_state
    import aws_sdk_medical_imaging.types.image_set_workflow_status
    import aws_sdk_medical_imaging.types.message
    import aws_sdk_medical_imaging.types.overrides


class ImageSetProperties(TypedDict):
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
    """<p>The timestamp when the image set properties were created.</p>"""
    updated_at: NotRequired["aws_sdk_medical_imaging.types.date.Date"]
    """<p>The timestamp when the image set properties were updated.</p>"""
    deleted_at: NotRequired["aws_sdk_medical_imaging.types.date.Date"]
    """<p>The timestamp when the image set properties were deleted.</p>"""
    message: NotRequired["aws_sdk_medical_imaging.types.message.Message"]
    """<p>The error message thrown if an image set action fails.</p>"""
    overrides: NotRequired["aws_sdk_medical_imaging.types.overrides.Overrides"]
    """<p>Contains details on overrides used when creating the returned version of an image set. For example, if <code>forced</code> exists, the <code>forced</code> flag was used when creating the image set.</p>"""
    is_primary: NotRequired["bool"]
    """<p>The flag to determine whether the image set is primary or not.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageSetProperties) -> dict:
    out: dict = {}
    out["imageSetId"] = value["image_set_id"]
    out["versionId"] = value["version_id"]
    import aws_sdk_medical_imaging.types.image_set_state

    out["imageSetState"] = aws_sdk_medical_imaging.types.image_set_state.serialize_json(
        value["image_set_state"]
    )
    if "image_set_workflow_status" in value:
        import aws_sdk_medical_imaging.types.image_set_workflow_status

        out["ImageSetWorkflowStatus"] = (
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
    if "overrides" in value:
        import aws_sdk_medical_imaging.types.overrides

        out["overrides"] = aws_sdk_medical_imaging.types.overrides.serialize_json(
            value["overrides"]
        )
    if "is_primary" in value:
        out["isPrimary"] = value["is_primary"]
    return out


def deserialize_json(data: dict) -> ImageSetProperties:
    out: ImageSetProperties = {}  # type: ignore[typeddict-item]
    if "imageSetId" in data:
        out["image_set_id"] = data["imageSetId"]
    else:
        raise DeserializationError("ImageSetProperties.image_set_id required")
    if "versionId" in data:
        out["version_id"] = data["versionId"]
    else:
        raise DeserializationError("ImageSetProperties.version_id required")
    if "imageSetState" in data:
        import aws_sdk_medical_imaging.types.image_set_state

        out["image_set_state"] = (
            aws_sdk_medical_imaging.types.image_set_state.deserialize_json(
                data["imageSetState"]
            )
        )
    else:
        raise DeserializationError("ImageSetProperties.image_set_state required")
    if "ImageSetWorkflowStatus" in data:
        import aws_sdk_medical_imaging.types.image_set_workflow_status

        out["image_set_workflow_status"] = (
            aws_sdk_medical_imaging.types.image_set_workflow_status.deserialize_json(
                data["ImageSetWorkflowStatus"]
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
    if "overrides" in data:
        import aws_sdk_medical_imaging.types.overrides

        out["overrides"] = aws_sdk_medical_imaging.types.overrides.deserialize_json(
            data["overrides"]
        )
    if "isPrimary" in data:
        out["is_primary"] = data["isPrimary"]
    return out
