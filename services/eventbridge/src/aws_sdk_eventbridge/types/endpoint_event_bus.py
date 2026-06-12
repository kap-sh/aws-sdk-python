"""Generated from Smithy shape ``com.amazonaws.eventbridge#EndpointEventBus``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.non_partner_event_bus_arn


class EndpointEventBus(TypedDict):
    event_bus_arn: (
        "aws_sdk_eventbridge.types.non_partner_event_bus_arn.NonPartnerEventBusArn"
    )
    """<p>The ARN of the event bus the endpoint is associated with.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointEventBus) -> dict:
    out: dict = {}
    out["EventBusArn"] = value["event_bus_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EndpointEventBus:
    out: EndpointEventBus = {}  # type: ignore[typeddict-item]
    if "EventBusArn" in data:
        out["event_bus_arn"] = data["EventBusArn"]
    else:
        raise DeserializationError("EndpointEventBus.event_bus_arn required")
    return out
