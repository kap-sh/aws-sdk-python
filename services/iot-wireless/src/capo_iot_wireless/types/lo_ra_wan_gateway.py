"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANGateway``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.beaconing
    import capo_iot_wireless.types.gateway_eui
    import capo_iot_wireless.types.gateway_max_eirp
    import capo_iot_wireless.types.join_eui_filters
    import capo_iot_wireless.types.net_id_filters
    import capo_iot_wireless.types.rf_region
    import capo_iot_wireless.types.sub_bands


class LoRaWANGateway(TypedDict, closed=True):
    gateway_eui: NotRequired["capo_iot_wireless.types.gateway_eui.GatewayEui"]
    """<p>The gateway's EUI value.</p>"""
    rf_region: NotRequired["capo_iot_wireless.types.rf_region.RfRegion"]
    """<p>The frequency band (RFRegion) value.</p>"""
    join_eui_filters: NotRequired[
        "capo_iot_wireless.types.join_eui_filters.JoinEuiFilters"
    ]
    net_id_filters: NotRequired["capo_iot_wireless.types.net_id_filters.NetIdFilters"]
    sub_bands: NotRequired["capo_iot_wireless.types.sub_bands.SubBands"]
    beaconing: NotRequired["capo_iot_wireless.types.beaconing.Beaconing"]
    """<p>Beaconing object information, which consists of the data rate and frequency parameters.</p>"""
    max_eirp: NotRequired["capo_iot_wireless.types.gateway_max_eirp.GatewayMaxEirp"]
    """<p>The MaxEIRP value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANGateway) -> dict:
    out: dict = {}
    if "gateway_eui" in value:
        out["GatewayEui"] = value["gateway_eui"]
    if "rf_region" in value:
        out["RfRegion"] = value["rf_region"]
    if "join_eui_filters" in value:
        import capo_iot_wireless.types.join_eui_filters

        out["JoinEuiFilters"] = capo_iot_wireless.types.join_eui_filters.serialize_json(
            value["join_eui_filters"]
        )
    if "net_id_filters" in value:
        import capo_iot_wireless.types.net_id_filters

        out["NetIdFilters"] = capo_iot_wireless.types.net_id_filters.serialize_json(
            value["net_id_filters"]
        )
    if "sub_bands" in value:
        import capo_iot_wireless.types.sub_bands

        out["SubBands"] = capo_iot_wireless.types.sub_bands.serialize_json(
            value["sub_bands"]
        )
    if "beaconing" in value:
        import capo_iot_wireless.types.beaconing

        out["Beaconing"] = capo_iot_wireless.types.beaconing.serialize_json(
            value["beaconing"]
        )
    if "max_eirp" in value:
        out["MaxEirp"] = value["max_eirp"]
    return out


def deserialize_json(data: dict) -> LoRaWANGateway:
    out: LoRaWANGateway = {}  # type: ignore[typeddict-item]
    if "GatewayEui" in data:
        out["gateway_eui"] = data["GatewayEui"]
    if "RfRegion" in data:
        out["rf_region"] = data["RfRegion"]
    if "JoinEuiFilters" in data:
        import capo_iot_wireless.types.join_eui_filters

        out["join_eui_filters"] = (
            capo_iot_wireless.types.join_eui_filters.deserialize_json(
                data["JoinEuiFilters"]
            )
        )
    if "NetIdFilters" in data:
        import capo_iot_wireless.types.net_id_filters

        out["net_id_filters"] = capo_iot_wireless.types.net_id_filters.deserialize_json(
            data["NetIdFilters"]
        )
    if "SubBands" in data:
        import capo_iot_wireless.types.sub_bands

        out["sub_bands"] = capo_iot_wireless.types.sub_bands.deserialize_json(
            data["SubBands"]
        )
    if "Beaconing" in data:
        import capo_iot_wireless.types.beaconing

        out["beaconing"] = capo_iot_wireless.types.beaconing.deserialize_json(
            data["Beaconing"]
        )
    if "MaxEirp" in data:
        out["max_eirp"] = data["MaxEirp"]
    return out
