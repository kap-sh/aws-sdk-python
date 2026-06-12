"""Generated from Smithy shape ``com.amazonaws.healthlake#DeleteFHIRDatastoreResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_healthlake.types.bounded_length_string
    import aws_sdk_healthlake.types.datastore_arn
    import aws_sdk_healthlake.types.datastore_id
    import aws_sdk_healthlake.types.datastore_status


class DeleteFHIRDatastoreResponse(TypedDict):
    datastore_id: "aws_sdk_healthlake.types.datastore_id.DatastoreId"
    """<p>The AWS-generated ID for the deleted data store.</p>"""
    datastore_arn: "aws_sdk_healthlake.types.datastore_arn.DatastoreArn"
    """<p>The Amazon Resource Name (ARN) that grants access permission to AWS HealthLake.</p>"""
    datastore_status: "aws_sdk_healthlake.types.datastore_status.DatastoreStatus"
    """<p>The data store status.</p>"""
    datastore_endpoint: (
        "aws_sdk_healthlake.types.bounded_length_string.BoundedLengthString"
    )
    """<p>The AWS endpoint of the data store to be deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteFHIRDatastoreResponse) -> dict:
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


def deserialize_aws_json_1_0(data: dict) -> DeleteFHIRDatastoreResponse:
    out: DeleteFHIRDatastoreResponse = {}  # type: ignore[typeddict-item]
    if "DatastoreId" in data:
        out["datastore_id"] = data["DatastoreId"]
    else:
        raise DeserializationError("DeleteFHIRDatastoreResponse.datastore_id required")
    if "DatastoreArn" in data:
        out["datastore_arn"] = data["DatastoreArn"]
    else:
        raise DeserializationError("DeleteFHIRDatastoreResponse.datastore_arn required")
    if "DatastoreStatus" in data:
        import aws_sdk_healthlake.types.datastore_status

        out["datastore_status"] = (
            aws_sdk_healthlake.types.datastore_status.deserialize_aws_json_1_0(
                data["DatastoreStatus"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteFHIRDatastoreResponse.datastore_status required"
        )
    if "DatastoreEndpoint" in data:
        out["datastore_endpoint"] = data["DatastoreEndpoint"]
    else:
        raise DeserializationError(
            "DeleteFHIRDatastoreResponse.datastore_endpoint required"
        )
    return out
