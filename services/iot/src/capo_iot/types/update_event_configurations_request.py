"""Generated from Smithy shape ``com.amazonaws.iot#UpdateEventConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.event_configurations


class UpdateEventConfigurationsRequest(TypedDict, closed=True):
    event_configurations: NotRequired[
        "capo_iot.types.event_configurations.EventConfigurations"
    ]
    """<p>The new event configuration values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEventConfigurationsRequest) -> dict:
    out: dict = {}
    if "event_configurations" in value:
        import capo_iot.types.event_configurations

        out["eventConfigurations"] = capo_iot.types.event_configurations.serialize_json(
            value["event_configurations"]
        )
    return out


def deserialize_json(data: dict) -> UpdateEventConfigurationsRequest:
    out: UpdateEventConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if "eventConfigurations" in data:
        import capo_iot.types.event_configurations

        out["event_configurations"] = (
            capo_iot.types.event_configurations.deserialize_json(
                data["eventConfigurations"]
            )
        )
    return out
