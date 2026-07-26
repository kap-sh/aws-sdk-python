"""Generated from Smithy shape ``com.amazonaws.healthlake#UpdateFHIRDatastoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_healthlake.types.datastore_properties


class UpdateFHIRDatastoreResponse(TypedDict, closed=True):
    datastore_properties: (
        "capo_healthlake.types.datastore_properties.DatastoreProperties"
    )
    """<para>The data store properties.</para>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateFHIRDatastoreResponse) -> dict:
    out: dict = {}
    import capo_healthlake.types.datastore_properties

    out["DatastoreProperties"] = (
        capo_healthlake.types.datastore_properties.serialize_aws_json_1_0(
            value["datastore_properties"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateFHIRDatastoreResponse:
    out: UpdateFHIRDatastoreResponse = {}  # type: ignore[typeddict-item]
    if "DatastoreProperties" in data:
        import capo_healthlake.types.datastore_properties

        out["datastore_properties"] = (
            capo_healthlake.types.datastore_properties.deserialize_aws_json_1_0(
                data["DatastoreProperties"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateFHIRDatastoreResponse.datastore_properties required"
        )
    return out
