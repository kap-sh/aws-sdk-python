"""Generated from Smithy shape ``com.amazonaws.iot#UpdateEventConfigurationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.event_configurations


class UpdateEventConfigurationsRequest(TypedDict):
    event_configurations: NotRequired[
        "aws_sdk_iot.types.event_configurations.EventConfigurations"
    ]
    """<p>The new event configuration values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEventConfigurationsRequest) -> dict:
    out: dict = {}
    if "event_configurations" in value:
        import aws_sdk_iot.types.event_configurations

        out["eventConfigurations"] = (
            aws_sdk_iot.types.event_configurations.serialize_json(
                value["event_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateEventConfigurationsRequest:
    out: UpdateEventConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if "eventConfigurations" in data:
        import aws_sdk_iot.types.event_configurations

        out["event_configurations"] = (
            aws_sdk_iot.types.event_configurations.deserialize_json(
                data["eventConfigurations"]
            )
        )
    return out
