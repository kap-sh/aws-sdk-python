"""Generated from Smithy shape ``com.amazonaws.medicalimaging#GetDatastoreResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.datastore_properties


class GetDatastoreResponse(TypedDict):
    datastore_properties: (
        "aws_sdk_medical_imaging.types.datastore_properties.DatastoreProperties"
    )
    """<p>The data store properties.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDatastoreResponse) -> dict:
    out: dict = {}
    import aws_sdk_medical_imaging.types.datastore_properties

    out["datastoreProperties"] = (
        aws_sdk_medical_imaging.types.datastore_properties.serialize_json(
            value["datastore_properties"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetDatastoreResponse:
    out: GetDatastoreResponse = {}  # type: ignore[typeddict-item]
    if "datastoreProperties" in data:
        import aws_sdk_medical_imaging.types.datastore_properties

        out["datastore_properties"] = (
            aws_sdk_medical_imaging.types.datastore_properties.deserialize_json(
                data["datastoreProperties"]
            )
        )
    else:
        raise DeserializationError("GetDatastoreResponse.datastore_properties required")
    return out
