"""Generated from Smithy shape ``com.amazonaws.iotwireless#DeviceRegistrationStateResourceTypeEventConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.sidewalk_resource_type_event_configuration


class DeviceRegistrationStateResourceTypeEventConfiguration(TypedDict, closed=True):
    sidewalk: NotRequired[
        "capo_iot_wireless.types.sidewalk_resource_type_event_configuration.SidewalkResourceTypeEventConfiguration"
    ]
    """<p>Device registration resource type state event configuration object for enabling or disabling Sidewalk related event topics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: DeviceRegistrationStateResourceTypeEventConfiguration,
) -> dict:
    out: dict = {}
    if "sidewalk" in value:
        import capo_iot_wireless.types.sidewalk_resource_type_event_configuration

        out["Sidewalk"] = (
            capo_iot_wireless.types.sidewalk_resource_type_event_configuration.serialize_json(
                value["sidewalk"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> DeviceRegistrationStateResourceTypeEventConfiguration:
    out: DeviceRegistrationStateResourceTypeEventConfiguration = {}  # type: ignore[typeddict-item]
    if "Sidewalk" in data:
        import capo_iot_wireless.types.sidewalk_resource_type_event_configuration

        out["sidewalk"] = (
            capo_iot_wireless.types.sidewalk_resource_type_event_configuration.deserialize_json(
                data["Sidewalk"]
            )
        )
    return out
