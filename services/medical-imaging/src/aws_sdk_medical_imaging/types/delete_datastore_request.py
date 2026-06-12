"""Generated from Smithy shape ``com.amazonaws.medicalimaging#DeleteDatastoreRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.datastore_id


class DeleteDatastoreRequest(TypedDict):
    datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDatastoreRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDatastoreRequest:
    out: DeleteDatastoreRequest = {}  # type: ignore[typeddict-item]
    return out
