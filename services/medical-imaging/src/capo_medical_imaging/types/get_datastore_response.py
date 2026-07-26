"""Generated from Smithy shape ``com.amazonaws.medicalimaging#GetDatastoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_medical_imaging.types.datastore_properties


class GetDatastoreResponse(TypedDict, closed=True):
    datastore_properties: (
        "capo_medical_imaging.types.datastore_properties.DatastoreProperties"
    )
    """<p>The data store properties.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDatastoreResponse) -> dict:
    out: dict = {}
    import capo_medical_imaging.types.datastore_properties

    out["datastoreProperties"] = (
        capo_medical_imaging.types.datastore_properties.serialize_json(
            value["datastore_properties"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetDatastoreResponse:
    out: GetDatastoreResponse = {}  # type: ignore[typeddict-item]
    if "datastoreProperties" in data:
        import capo_medical_imaging.types.datastore_properties

        out["datastore_properties"] = (
            capo_medical_imaging.types.datastore_properties.deserialize_json(
                data["datastoreProperties"]
            )
        )
    else:
        raise DeserializationError("GetDatastoreResponse.datastore_properties required")
    return out
