"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANGatewayVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.model
    import capo_iot_wireless.types.package_version
    import capo_iot_wireless.types.station


class LoRaWANGatewayVersion(TypedDict, closed=True):
    package_version: NotRequired[
        "capo_iot_wireless.types.package_version.PackageVersion"
    ]
    """<p>The version of the wireless gateway firmware.</p>"""
    model: NotRequired["capo_iot_wireless.types.model.Model"]
    """<p>The model number of the wireless gateway.</p>"""
    station: NotRequired["capo_iot_wireless.types.station.Station"]
    """<p>The basic station version of the wireless gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANGatewayVersion) -> dict:
    out: dict = {}
    if "package_version" in value:
        out["PackageVersion"] = value["package_version"]
    if "model" in value:
        out["Model"] = value["model"]
    if "station" in value:
        out["Station"] = value["station"]
    return out


def deserialize_json(data: dict) -> LoRaWANGatewayVersion:
    out: LoRaWANGatewayVersion = {}  # type: ignore[typeddict-item]
    if "PackageVersion" in data:
        out["package_version"] = data["PackageVersion"]
    if "Model" in data:
        out["model"] = data["Model"]
    if "Station" in data:
        out["station"] = data["Station"]
    return out
