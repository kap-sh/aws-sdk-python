"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEventsEndpointEventBusesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_events_endpoint_event_buses_details

AwsEventsEndpointEventBusesList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_events_endpoint_event_buses_details.AwsEventsEndpointEventBusesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEventsEndpointEventBusesList) -> list:
    import aws_sdk_securityhub.types.aws_events_endpoint_event_buses_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_events_endpoint_event_buses_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEventsEndpointEventBusesList:
    import aws_sdk_securityhub.types.aws_events_endpoint_event_buses_details

    out: AwsEventsEndpointEventBusesList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_events_endpoint_event_buses_details.deserialize_json(
                item
            )
        )
    return out
