"""Generated from Smithy shape ``com.amazonaws.chime#GetEventsConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime.types.events_configuration


class GetEventsConfigurationResponse(TypedDict):
    events_configuration: NotRequired[
        "aws_sdk_chime.types.events_configuration.EventsConfiguration"
    ]
    """<p>The events configuration details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEventsConfigurationResponse) -> dict:
    out: dict = {}
    if "events_configuration" in value:
        import aws_sdk_chime.types.events_configuration

        out["EventsConfiguration"] = (
            aws_sdk_chime.types.events_configuration.serialize_json(
                value["events_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetEventsConfigurationResponse:
    out: GetEventsConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "EventsConfiguration" in data:
        import aws_sdk_chime.types.events_configuration

        out["events_configuration"] = (
            aws_sdk_chime.types.events_configuration.deserialize_json(
                data["EventsConfiguration"]
            )
        )
    return out
