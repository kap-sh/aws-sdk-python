"""Generated from Smithy shape ``com.amazonaws.medicalimaging#GetDatastoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_medical_imaging.types.datastore_id


class GetDatastoreRequest(TypedDict, closed=True):
    datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDatastoreRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDatastoreRequest:
    out: GetDatastoreRequest = {}  # type: ignore[typeddict-item]
    return out
