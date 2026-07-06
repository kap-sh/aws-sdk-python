"""Generated from Smithy shape ``com.amazonaws.medicalimaging#CopySourceImageSetProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.arn
    import aws_sdk_medical_imaging.types.date
    import aws_sdk_medical_imaging.types.image_set_external_version_id
    import aws_sdk_medical_imaging.types.image_set_id
    import aws_sdk_medical_imaging.types.image_set_state
    import aws_sdk_medical_imaging.types.image_set_workflow_status


class CopySourceImageSetProperties(TypedDict, closed=True):
    image_set_id: "aws_sdk_medical_imaging.types.image_set_id.ImageSetId"
    """<p>The image set identifier for the copied source image set.</p>"""
    latest_version_id: "aws_sdk_medical_imaging.types.image_set_external_version_id.ImageSetExternalVersionId"
    """<p>The latest version identifier for the copied source image set.</p>"""
    image_set_state: NotRequired[
        "aws_sdk_medical_imaging.types.image_set_state.ImageSetState"
    ]
    """<p>The image set state of the copied source image set.</p>"""
    image_set_workflow_status: NotRequired[
        "aws_sdk_medical_imaging.types.image_set_workflow_status.ImageSetWorkflowStatus"
    ]
    """<p>The workflow status of the copied source image set.</p>"""
    created_at: NotRequired["aws_sdk_medical_imaging.types.date.Date"]
    """<p>The timestamp when the source image set properties were created.</p>"""
    updated_at: NotRequired["aws_sdk_medical_imaging.types.date.Date"]
    """<p>The timestamp when the source image set properties were updated.</p>"""
    image_set_arn: NotRequired["aws_sdk_medical_imaging.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) assigned to the source image set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CopySourceImageSetProperties) -> dict:
    out: dict = {}
    out["imageSetId"] = value["image_set_id"]
    out["latestVersionId"] = value["latest_version_id"]
    if "image_set_state" in value:
        import aws_sdk_medical_imaging.types.image_set_state

        out["imageSetState"] = (
            aws_sdk_medical_imaging.types.image_set_state.serialize_json(
                value["image_set_state"]
            )
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
    if "image_set_arn" in value:
        out["imageSetArn"] = value["image_set_arn"]
    return out


def deserialize_json(data: dict) -> CopySourceImageSetProperties:
    out: CopySourceImageSetProperties = {}  # type: ignore[typeddict-item]
    if "imageSetId" in data:
        out["image_set_id"] = data["imageSetId"]
    else:
        raise DeserializationError("CopySourceImageSetProperties.image_set_id required")
    if "latestVersionId" in data:
        out["latest_version_id"] = data["latestVersionId"]
    else:
        raise DeserializationError(
            "CopySourceImageSetProperties.latest_version_id required"
        )
    if "imageSetState" in data:
        import aws_sdk_medical_imaging.types.image_set_state

        out["image_set_state"] = (
            aws_sdk_medical_imaging.types.image_set_state.deserialize_json(
                data["imageSetState"]
            )
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
    if "imageSetArn" in data:
        out["image_set_arn"] = data["imageSetArn"]
    return out
