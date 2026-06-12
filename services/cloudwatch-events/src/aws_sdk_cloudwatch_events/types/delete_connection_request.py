"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#DeleteConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudwatch_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.connection_name


class DeleteConnectionRequest(TypedDict):
    name: "aws_sdk_cloudwatch_events.types.connection_name.ConnectionName"
    """<p>The name of the connection to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteConnectionRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteConnectionRequest:
    out: DeleteConnectionRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeleteConnectionRequest.name required")
    return out
