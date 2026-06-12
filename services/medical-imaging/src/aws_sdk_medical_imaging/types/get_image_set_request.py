"""Generated from Smithy shape ``com.amazonaws.medicalimaging#GetImageSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.datastore_id
    import aws_sdk_medical_imaging.types.image_set_external_version_id
    import aws_sdk_medical_imaging.types.image_set_id


class GetImageSetRequest(TypedDict):
    datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    image_set_id: "aws_sdk_medical_imaging.types.image_set_id.ImageSetId"
    """<p>The image set identifier.</p>"""
    version_id: NotRequired[
        "aws_sdk_medical_imaging.types.image_set_external_version_id.ImageSetExternalVersionId"
    ]
    """<p>The image set version identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImageSetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetImageSetRequest:
    out: GetImageSetRequest = {}  # type: ignore[typeddict-item]
    return out
