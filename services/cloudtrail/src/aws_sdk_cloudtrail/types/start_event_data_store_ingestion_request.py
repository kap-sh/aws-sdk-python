"""Generated from Smithy shape ``com.amazonaws.cloudtrail#StartEventDataStoreIngestionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.event_data_store_arn


class StartEventDataStoreIngestionRequest(TypedDict):
    event_data_store: "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
    """<p>The ARN (or ID suffix of the ARN) of the event data store for which you want to start ingestion.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartEventDataStoreIngestionRequest) -> dict:
    out: dict = {}
    out["EventDataStore"] = value["event_data_store"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartEventDataStoreIngestionRequest:
    out: StartEventDataStoreIngestionRequest = {}  # type: ignore[typeddict-item]
    if "EventDataStore" in data:
        out["event_data_store"] = data["EventDataStore"]
    else:
        raise DeserializationError(
            "StartEventDataStoreIngestionRequest.event_data_store required"
        )
    return out
