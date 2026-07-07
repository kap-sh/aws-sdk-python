"""Generated from Smithy shape ``com.amazonaws.eventbridge#DeleteApiDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.api_destination_name


class DeleteApiDestinationRequest(TypedDict, closed=True):
    name: "aws_sdk_eventbridge.types.api_destination_name.ApiDestinationName"
    """<p>The name of the destination to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteApiDestinationRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteApiDestinationRequest:
    out: DeleteApiDestinationRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeleteApiDestinationRequest.name required")
    return out
