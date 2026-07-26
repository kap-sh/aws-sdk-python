"""Generated from Smithy shape ``com.amazonaws.iotwireless#ProximityResourceTypeEventConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.sidewalk_resource_type_event_configuration


class ProximityResourceTypeEventConfiguration(TypedDict, closed=True):
    sidewalk: NotRequired[
        "capo_iot_wireless.types.sidewalk_resource_type_event_configuration.SidewalkResourceTypeEventConfiguration"
    ]
    """<p>Proximity resource type event configuration object for enabling and disabling wireless device topic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProximityResourceTypeEventConfiguration) -> dict:
    out: dict = {}
    if "sidewalk" in value:
        import capo_iot_wireless.types.sidewalk_resource_type_event_configuration

        out["Sidewalk"] = (
            capo_iot_wireless.types.sidewalk_resource_type_event_configuration.serialize_json(
                value["sidewalk"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProximityResourceTypeEventConfiguration:
    out: ProximityResourceTypeEventConfiguration = {}  # type: ignore[typeddict-item]
    if "Sidewalk" in data:
        import capo_iot_wireless.types.sidewalk_resource_type_event_configuration

        out["sidewalk"] = (
            capo_iot_wireless.types.sidewalk_resource_type_event_configuration.deserialize_json(
                data["Sidewalk"]
            )
        )
    return out
