"""Generated from Smithy shape ``com.amazonaws.medicalimaging#DeleteImageSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.datastore_id
    import aws_sdk_medical_imaging.types.image_set_id


class DeleteImageSetRequest(TypedDict):
    datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    image_set_id: "aws_sdk_medical_imaging.types.image_set_id.ImageSetId"
    """<p>The image set identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteImageSetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteImageSetRequest:
    out: DeleteImageSetRequest = {}  # type: ignore[typeddict-item]
    return out
