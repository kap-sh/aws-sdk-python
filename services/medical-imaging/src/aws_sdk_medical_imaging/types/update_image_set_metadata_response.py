"""Generated from Smithy shape ``com.amazonaws.medicalimaging#UpdateImageSetMetadataResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.datastore_id
    import aws_sdk_medical_imaging.types.date
    import aws_sdk_medical_imaging.types.image_set_external_version_id
    import aws_sdk_medical_imaging.types.image_set_id
    import aws_sdk_medical_imaging.types.image_set_state
    import aws_sdk_medical_imaging.types.image_set_workflow_status
    import aws_sdk_medical_imaging.types.message


class UpdateImageSetMetadataResponse(TypedDict):
    datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    image_set_id: "aws_sdk_medical_imaging.types.image_set_id.ImageSetId"
    """<p>The image set identifier.</p>"""
    latest_version_id: "aws_sdk_medical_imaging.types.image_set_external_version_id.ImageSetExternalVersionId"
    """<p>The latest image set version identifier.</p>"""
    image_set_state: "aws_sdk_medical_imaging.types.image_set_state.ImageSetState"
    """<p>The image set state.</p>"""
    image_set_workflow_status: NotRequired[
        "aws_sdk_medical_imaging.types.image_set_workflow_status.ImageSetWorkflowStatus"
    ]
    """<p>The image set workflow status.</p>"""
    created_at: NotRequired["aws_sdk_medical_imaging.types.date.Date"]
    """<p>The timestamp when image set metadata was created.</p>"""
    updated_at: NotRequired["aws_sdk_medical_imaging.types.date.Date"]
    """<p>The timestamp when image set metadata was updated.</p>"""
    message: NotRequired["aws_sdk_medical_imaging.types.message.Message"]
    """<p>The error message thrown if an update image set metadata action fails.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateImageSetMetadataResponse) -> dict:
    out: dict = {}
    out["datastoreId"] = value["datastore_id"]
    out["imageSetId"] = value["image_set_id"]
    out["latestVersionId"] = value["latest_version_id"]
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
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UpdateImageSetMetadataResponse:
    out: UpdateImageSetMetadataResponse = {}  # type: ignore[typeddict-item]
    if "datastoreId" in data:
        out["datastore_id"] = data["datastoreId"]
    else:
        raise DeserializationError(
            "UpdateImageSetMetadataResponse.datastore_id required"
        )
    if "imageSetId" in data:
        out["image_set_id"] = data["imageSetId"]
    else:
        raise DeserializationError(
            "UpdateImageSetMetadataResponse.image_set_id required"
        )
    if "latestVersionId" in data:
        out["latest_version_id"] = data["latestVersionId"]
    else:
        raise DeserializationError(
            "UpdateImageSetMetadataResponse.latest_version_id required"
        )
    if "imageSetState" in data:
        import aws_sdk_medical_imaging.types.image_set_state

        out["image_set_state"] = (
            aws_sdk_medical_imaging.types.image_set_state.deserialize_json(
                data["imageSetState"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateImageSetMetadataResponse.image_set_state required"
        )
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
    if "message" in data:
        out["message"] = data["message"]
    return out
