"""Generated from Smithy shape ``com.amazonaws.connect#Customer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.device_info
    import capo_connect.types.participant_capabilities


class Customer(TypedDict, closed=True):
    device_info: NotRequired["capo_connect.types.device_info.DeviceInfo"]
    """<p>Information regarding Customer’s device.</p>"""
    capabilities: NotRequired[
        "capo_connect.types.participant_capabilities.ParticipantCapabilities"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: Customer) -> dict:
    out: dict = {}
    if "device_info" in value:
        import capo_connect.types.device_info

        out["DeviceInfo"] = capo_connect.types.device_info.serialize_json(
            value["device_info"]
        )
    if "capabilities" in value:
        import capo_connect.types.participant_capabilities

        out["Capabilities"] = (
            capo_connect.types.participant_capabilities.serialize_json(
                value["capabilities"]
            )
        )
    return out


def deserialize_json(data: dict) -> Customer:
    out: Customer = {}  # type: ignore[typeddict-item]
    if "DeviceInfo" in data:
        import capo_connect.types.device_info

        out["device_info"] = capo_connect.types.device_info.deserialize_json(
            data["DeviceInfo"]
        )
    if "Capabilities" in data:
        import capo_connect.types.participant_capabilities

        out["capabilities"] = (
            capo_connect.types.participant_capabilities.deserialize_json(
                data["Capabilities"]
            )
        )
    return out
