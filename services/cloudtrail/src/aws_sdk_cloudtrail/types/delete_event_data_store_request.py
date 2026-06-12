"""Generated from Smithy shape ``com.amazonaws.cloudtrail#DeleteEventDataStoreRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.event_data_store_arn


class DeleteEventDataStoreRequest(TypedDict):
    event_data_store: "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
    """<p>The ARN (or the ID suffix of the ARN) of the event data store to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEventDataStoreRequest) -> dict:
    out: dict = {}
    out["EventDataStore"] = value["event_data_store"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEventDataStoreRequest:
    out: DeleteEventDataStoreRequest = {}  # type: ignore[typeddict-item]
    if "EventDataStore" in data:
        out["event_data_store"] = data["EventDataStore"]
    else:
        raise DeserializationError(
            "DeleteEventDataStoreRequest.event_data_store required"
        )
    return out
