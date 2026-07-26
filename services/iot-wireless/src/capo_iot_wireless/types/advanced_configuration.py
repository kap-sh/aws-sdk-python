"""Generated from Smithy shape ``com.amazonaws.iotwireless#AdvancedConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.wi_fi_cellular


class AdvancedConfiguration(TypedDict, closed=True):
    wi_fi_cellular: NotRequired["capo_iot_wireless.types.wi_fi_cellular.WiFiCellular"]
    """Configuration for WiFi and cellular-based payloads for location estimates."""


# --- restJson1 ser/de ---
def serialize_json(value: AdvancedConfiguration) -> dict:
    out: dict = {}
    if "wi_fi_cellular" in value:
        import capo_iot_wireless.types.wi_fi_cellular

        out["WiFiCellular"] = capo_iot_wireless.types.wi_fi_cellular.serialize_json(
            value["wi_fi_cellular"]
        )
    return out


def deserialize_json(data: dict) -> AdvancedConfiguration:
    out: AdvancedConfiguration = {}  # type: ignore[typeddict-item]
    if "WiFiCellular" in data:
        import capo_iot_wireless.types.wi_fi_cellular

        out["wi_fi_cellular"] = capo_iot_wireless.types.wi_fi_cellular.deserialize_json(
            data["WiFiCellular"]
        )
    return out
