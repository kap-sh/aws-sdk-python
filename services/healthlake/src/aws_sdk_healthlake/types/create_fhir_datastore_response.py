"""Generated from Smithy shape ``com.amazonaws.healthlake#CreateFHIRDatastoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_healthlake.types.bounded_length_string
    import aws_sdk_healthlake.types.datastore_arn
    import aws_sdk_healthlake.types.datastore_id
    import aws_sdk_healthlake.types.datastore_status


class CreateFHIRDatastoreResponse(TypedDict, closed=True):
    datastore_id: "aws_sdk_healthlake.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    datastore_arn: "aws_sdk_healthlake.types.datastore_arn.DatastoreArn"
    """<p>The Amazon Resource Name (ARN) for the data store.</p>"""
    datastore_status: "aws_sdk_healthlake.types.datastore_status.DatastoreStatus"
    """<p>The data store status.</p>"""
    datastore_endpoint: (
        "aws_sdk_healthlake.types.bounded_length_string.BoundedLengthString"
    )
    """<p>The AWS endpoint created for the data store.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateFHIRDatastoreResponse) -> dict:
    out: dict = {}
    out["DatastoreId"] = value["datastore_id"]
    out["DatastoreArn"] = value["datastore_arn"]
    import aws_sdk_healthlake.types.datastore_status

    out["DatastoreStatus"] = (
        aws_sdk_healthlake.types.datastore_status.serialize_aws_json_1_0(
            value["datastore_status"]
        )
    )
    out["DatastoreEndpoint"] = value["datastore_endpoint"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateFHIRDatastoreResponse:
    out: CreateFHIRDatastoreResponse = {}  # type: ignore[typeddict-item]
    if "DatastoreId" in data:
        out["datastore_id"] = data["DatastoreId"]
    else:
        raise DeserializationError("CreateFHIRDatastoreResponse.datastore_id required")
    if "DatastoreArn" in data:
        out["datastore_arn"] = data["DatastoreArn"]
    else:
        raise DeserializationError("CreateFHIRDatastoreResponse.datastore_arn required")
    if "DatastoreStatus" in data:
        import aws_sdk_healthlake.types.datastore_status

        out["datastore_status"] = (
            aws_sdk_healthlake.types.datastore_status.deserialize_aws_json_1_0(
                data["DatastoreStatus"]
            )
        )
    else:
        raise DeserializationError(
            "CreateFHIRDatastoreResponse.datastore_status required"
        )
    if "DatastoreEndpoint" in data:
        out["datastore_endpoint"] = data["DatastoreEndpoint"]
    else:
        raise DeserializationError(
            "CreateFHIRDatastoreResponse.datastore_endpoint required"
        )
    return out
