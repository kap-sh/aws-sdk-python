"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEventsEndpointEventBusesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_events_endpoint_event_buses_details

AwsEventsEndpointEventBusesList: TypeAlias = list[
    "capo_securityhub.types.aws_events_endpoint_event_buses_details.AwsEventsEndpointEventBusesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEventsEndpointEventBusesList) -> list:
    import capo_securityhub.types.aws_events_endpoint_event_buses_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_events_endpoint_event_buses_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEventsEndpointEventBusesList:
    import capo_securityhub.types.aws_events_endpoint_event_buses_details

    out: AwsEventsEndpointEventBusesList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_events_endpoint_event_buses_details.deserialize_json(
                item
            )
        )
    return out
