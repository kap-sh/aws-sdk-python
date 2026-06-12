"""Generated from Smithy shape ``com.amazonaws.frauddetector#DeleteEventsByEventTypeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.identifier


class DeleteEventsByEventTypeRequest(TypedDict):
    event_type_name: "aws_sdk_frauddetector.types.identifier.identifier"
    """<p>The name of the event type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEventsByEventTypeRequest) -> dict:
    out: dict = {}
    out["eventTypeName"] = value["event_type_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEventsByEventTypeRequest:
    out: DeleteEventsByEventTypeRequest = {}  # type: ignore[typeddict-item]
    if "eventTypeName" in data:
        out["event_type_name"] = data["eventTypeName"]
    else:
        raise DeserializationError(
            "DeleteEventsByEventTypeRequest.event_type_name required"
        )
    return out
