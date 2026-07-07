"""Generated from Smithy shape ``com.amazonaws.cloudtrail#GetEventDataStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.event_data_store_arn


class GetEventDataStoreRequest(TypedDict, closed=True):
    event_data_store: "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
    """<p>The ARN (or ID suffix of the ARN) of the event data store about which you want information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetEventDataStoreRequest) -> dict:
    out: dict = {}
    out["EventDataStore"] = value["event_data_store"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetEventDataStoreRequest:
    out: GetEventDataStoreRequest = {}  # type: ignore[typeddict-item]
    if "EventDataStore" in data:
        out["event_data_store"] = data["EventDataStore"]
    else:
        raise DeserializationError("GetEventDataStoreRequest.event_data_store required")
    return out
