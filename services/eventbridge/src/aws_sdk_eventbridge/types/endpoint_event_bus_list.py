"""Generated from Smithy shape ``com.amazonaws.eventbridge#EndpointEventBusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.endpoint_event_bus

EndpointEventBusList: TypeAlias = list[
    "aws_sdk_eventbridge.types.endpoint_event_bus.EndpointEventBus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointEventBusList) -> list:
    import aws_sdk_eventbridge.types.endpoint_event_bus

    out: list = []
    for item in value:
        out.append(
            aws_sdk_eventbridge.types.endpoint_event_bus.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EndpointEventBusList:
    import aws_sdk_eventbridge.types.endpoint_event_bus

    out: EndpointEventBusList = []
    for item in data:
        out.append(
            aws_sdk_eventbridge.types.endpoint_event_bus.deserialize_aws_json_1_1(item)
        )
    return out
