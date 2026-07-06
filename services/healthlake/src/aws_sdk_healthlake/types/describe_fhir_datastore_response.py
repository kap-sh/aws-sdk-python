"""Generated from Smithy shape ``com.amazonaws.healthlake#DescribeFHIRDatastoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_healthlake.types.datastore_properties


class DescribeFHIRDatastoreResponse(TypedDict, closed=True):
    datastore_properties: (
        "aws_sdk_healthlake.types.datastore_properties.DatastoreProperties"
    )
    """<p>The data store properties.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeFHIRDatastoreResponse) -> dict:
    out: dict = {}
    import aws_sdk_healthlake.types.datastore_properties

    out["DatastoreProperties"] = (
        aws_sdk_healthlake.types.datastore_properties.serialize_aws_json_1_0(
            value["datastore_properties"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeFHIRDatastoreResponse:
    out: DescribeFHIRDatastoreResponse = {}  # type: ignore[typeddict-item]
    if "DatastoreProperties" in data:
        import aws_sdk_healthlake.types.datastore_properties

        out["datastore_properties"] = (
            aws_sdk_healthlake.types.datastore_properties.deserialize_aws_json_1_0(
                data["DatastoreProperties"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeFHIRDatastoreResponse.datastore_properties required"
        )
    return out
