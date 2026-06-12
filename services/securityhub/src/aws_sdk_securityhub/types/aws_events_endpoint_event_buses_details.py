"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEventsEndpointEventBusesDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEventsEndpointEventBusesDetails(TypedDict):
    event_bus_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) of the event bus that the endpoint is associated with.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEventsEndpointEventBusesDetails) -> dict:
    out: dict = {}
    if "event_bus_arn" in value:
        out["EventBusArn"] = value["event_bus_arn"]
    return out


def deserialize_json(data: dict) -> AwsEventsEndpointEventBusesDetails:
    out: AwsEventsEndpointEventBusesDetails = {}  # type: ignore[typeddict-item]
    if "EventBusArn" in data:
        out["event_bus_arn"] = data["EventBusArn"]
    return out
