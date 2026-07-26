"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetPositionEstimateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.advanced_configuration
    import capo_iot_wireless.types.cell_towers
    import capo_iot_wireless.types.creation_date
    import capo_iot_wireless.types.gnss
    import capo_iot_wireless.types.ip
    import capo_iot_wireless.types.wi_fi_access_points


class GetPositionEstimateRequest(TypedDict, closed=True):
    wi_fi_access_points: NotRequired[
        "capo_iot_wireless.types.wi_fi_access_points.WiFiAccessPoints"
    ]
    """<p>Retrieves an estimated device position by resolving WLAN measurement data. The position is resolved using HERE's Wi-Fi based solver.</p>"""
    cell_towers: NotRequired["capo_iot_wireless.types.cell_towers.CellTowers"]
    """<p>Retrieves an estimated device position by resolving measurement data from cellular radio towers. The position is resolved using HERE's cellular-based solver.</p>"""
    ip: NotRequired["capo_iot_wireless.types.ip.Ip"]
    """<p>Retrieves an estimated device position by resolving the IP address information from the device. The position is resolved using MaxMind's IP-based solver.</p>"""
    gnss: NotRequired["capo_iot_wireless.types.gnss.Gnss"]
    """<p>Retrieves an estimated device position by resolving the global navigation satellite system (GNSS) scan data. The position is resolved using the GNSS solver powered by LoRa Cloud.</p>"""
    timestamp: NotRequired["capo_iot_wireless.types.creation_date.CreationDate"]
    """<p>Optional information that specifies the time when the position information will be resolved. It uses the Unix timestamp format. If not specified, the time at which the request was received will be used.</p>"""
    advanced_configuration: NotRequired[
        "capo_iot_wireless.types.advanced_configuration.AdvancedConfiguration"
    ]
    """Optional configuration to customize position estimates. If not provided, defaults are applied."""


# --- restJson1 ser/de ---
def serialize_json(value: GetPositionEstimateRequest) -> dict:
    out: dict = {}
    if "wi_fi_access_points" in value:
        import capo_iot_wireless.types.wi_fi_access_points

        out["WiFiAccessPoints"] = (
            capo_iot_wireless.types.wi_fi_access_points.serialize_json(
                value["wi_fi_access_points"]
            )
        )
    if "cell_towers" in value:
        import capo_iot_wireless.types.cell_towers

        out["CellTowers"] = capo_iot_wireless.types.cell_towers.serialize_json(
            value["cell_towers"]
        )
    if "ip" in value:
        import capo_iot_wireless.types.ip

        out["Ip"] = capo_iot_wireless.types.ip.serialize_json(value["ip"])
    if "gnss" in value:
        import capo_iot_wireless.types.gnss

        out["Gnss"] = capo_iot_wireless.types.gnss.serialize_json(value["gnss"])
    if "timestamp" in value:
        import capo_iot_wireless.types.creation_date

        out["Timestamp"] = capo_iot_wireless.types.creation_date.serialize_json(
            value["timestamp"]
        )
    if "advanced_configuration" in value:
        import capo_iot_wireless.types.advanced_configuration

        out["AdvancedConfiguration"] = (
            capo_iot_wireless.types.advanced_configuration.serialize_json(
                value["advanced_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetPositionEstimateRequest:
    out: GetPositionEstimateRequest = {}  # type: ignore[typeddict-item]
    if "WiFiAccessPoints" in data:
        import capo_iot_wireless.types.wi_fi_access_points

        out["wi_fi_access_points"] = (
            capo_iot_wireless.types.wi_fi_access_points.deserialize_json(
                data["WiFiAccessPoints"]
            )
        )
    if "CellTowers" in data:
        import capo_iot_wireless.types.cell_towers

        out["cell_towers"] = capo_iot_wireless.types.cell_towers.deserialize_json(
            data["CellTowers"]
        )
    if "Ip" in data:
        import capo_iot_wireless.types.ip

        out["ip"] = capo_iot_wireless.types.ip.deserialize_json(data["Ip"])
    if "Gnss" in data:
        import capo_iot_wireless.types.gnss

        out["gnss"] = capo_iot_wireless.types.gnss.deserialize_json(data["Gnss"])
    if "Timestamp" in data:
        import capo_iot_wireless.types.creation_date

        out["timestamp"] = capo_iot_wireless.types.creation_date.deserialize_json(
            data["Timestamp"]
        )
    if "AdvancedConfiguration" in data:
        import capo_iot_wireless.types.advanced_configuration

        out["advanced_configuration"] = (
            capo_iot_wireless.types.advanced_configuration.deserialize_json(
                data["AdvancedConfiguration"]
            )
        )
    return out
