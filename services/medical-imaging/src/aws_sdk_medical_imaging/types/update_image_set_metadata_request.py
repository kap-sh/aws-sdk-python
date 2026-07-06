"""Generated from Smithy shape ``com.amazonaws.medicalimaging#UpdateImageSetMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.datastore_id
    import aws_sdk_medical_imaging.types.image_set_external_version_id
    import aws_sdk_medical_imaging.types.image_set_id
    import aws_sdk_medical_imaging.types.metadata_updates


class UpdateImageSetMetadataRequest(TypedDict, closed=True):
    datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    image_set_id: "aws_sdk_medical_imaging.types.image_set_id.ImageSetId"
    """<p>The image set identifier.</p>"""
    latest_version_id: "aws_sdk_medical_imaging.types.image_set_external_version_id.ImageSetExternalVersionId"
    """<p>The latest image set version identifier.</p>"""
    force: NotRequired["bool"]
    """<p>Setting this flag will force the <code>UpdateImageSetMetadata</code> operation for the following attributes:</p> <ul> <li> <p> <code>Tag.StudyInstanceUID</code>, <code>Tag.SeriesInstanceUID</code>, <code>Tag.SOPInstanceUID</code>, and <code>Tag.StudyID</code> </p> </li> <li> <p>Adding, removing, or updating private tags for an individual SOP Instance</p> </li> </ul>"""
    include_study_image_sets: NotRequired["bool"]
    """<p>Flag to apply the metadata updates to all image sets in the same Study as the requested image set ID.</p>"""
    update_image_set_metadata_updates: (
        "aws_sdk_medical_imaging.types.metadata_updates.MetadataUpdates"
    )
    """<p>Update image set metadata updates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateImageSetMetadataRequest) -> dict:
    out: dict = {}
    import aws_sdk_medical_imaging.types.metadata_updates

    out["updateImageSetMetadataUpdates"] = (
        aws_sdk_medical_imaging.types.metadata_updates.serialize_json(
            value["update_image_set_metadata_updates"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateImageSetMetadataRequest:
    out: UpdateImageSetMetadataRequest = {}  # type: ignore[typeddict-item]
    if "updateImageSetMetadataUpdates" in data:
        import aws_sdk_medical_imaging.types.metadata_updates

        out["update_image_set_metadata_updates"] = (
            aws_sdk_medical_imaging.types.metadata_updates.deserialize_json(
                data["updateImageSetMetadataUpdates"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateImageSetMetadataRequest.update_image_set_metadata_updates required"
        )
    return out
