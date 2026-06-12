"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetDeleteEventsByEventTypeStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.identifier


class GetDeleteEventsByEventTypeStatusRequest(TypedDict):
    event_type_name: "aws_sdk_frauddetector.types.identifier.identifier"
    """<p>Name of event type for which to get the deletion status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeleteEventsByEventTypeStatusRequest) -> dict:
    out: dict = {}
    out["eventTypeName"] = value["event_type_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeleteEventsByEventTypeStatusRequest:
    out: GetDeleteEventsByEventTypeStatusRequest = {}  # type: ignore[typeddict-item]
    if "eventTypeName" in data:
        out["event_type_name"] = data["eventTypeName"]
    else:
        raise DeserializationError(
            "GetDeleteEventsByEventTypeStatusRequest.event_type_name required"
        )
    return out
