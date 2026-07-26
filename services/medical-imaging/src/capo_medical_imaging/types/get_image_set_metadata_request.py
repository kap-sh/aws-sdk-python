"""Generated from Smithy shape ``com.amazonaws.medicalimaging#GetImageSetMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medical_imaging.types.datastore_id
    import capo_medical_imaging.types.image_set_external_version_id
    import capo_medical_imaging.types.image_set_id


class GetImageSetMetadataRequest(TypedDict, closed=True):
    datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    image_set_id: "capo_medical_imaging.types.image_set_id.ImageSetId"
    """<p>The image set identifier.</p>"""
    version_id: NotRequired[
        "capo_medical_imaging.types.image_set_external_version_id.ImageSetExternalVersionId"
    ]
    """<p>The image set version identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImageSetMetadataRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetImageSetMetadataRequest:
    out: GetImageSetMetadataRequest = {}  # type: ignore[typeddict-item]
    return out
