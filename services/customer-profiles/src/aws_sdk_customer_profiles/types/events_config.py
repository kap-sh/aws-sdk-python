"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EventsConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.event_parameters_list


class EventsConfig(TypedDict):
    event_parameters_list: (
        "aws_sdk_customer_profiles.types.event_parameters_list.EventParametersList"
    )
    """<p>A list of event parameters configurations that specify how different event types should be handled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventsConfig) -> dict:
    out: dict = {}
    import aws_sdk_customer_profiles.types.event_parameters_list

    out["EventParametersList"] = (
        aws_sdk_customer_profiles.types.event_parameters_list.serialize_json(
            value["event_parameters_list"]
        )
    )
    return out


def deserialize_json(data: dict) -> EventsConfig:
    out: EventsConfig = {}  # type: ignore[typeddict-item]
    if "EventParametersList" in data:
        import aws_sdk_customer_profiles.types.event_parameters_list

        out["event_parameters_list"] = (
            aws_sdk_customer_profiles.types.event_parameters_list.deserialize_json(
                data["EventParametersList"]
            )
        )
    else:
        raise DeserializationError("EventsConfig.event_parameters_list required")
    return out
