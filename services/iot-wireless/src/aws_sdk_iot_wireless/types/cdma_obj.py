"""Generated from Smithy shape ``com.amazonaws.iotwireless#CdmaObj``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.base_lat
    import aws_sdk_iot_wireless.types.base_lng
    import aws_sdk_iot_wireless.types.base_station_id
    import aws_sdk_iot_wireless.types.cdma_local_id
    import aws_sdk_iot_wireless.types.cdma_nmr_list
    import aws_sdk_iot_wireless.types.network_id
    import aws_sdk_iot_wireless.types.pilot_power
    import aws_sdk_iot_wireless.types.registration_zone
    import aws_sdk_iot_wireless.types.system_id


class CdmaObj(TypedDict):
    system_id: "aws_sdk_iot_wireless.types.system_id.SystemId"
    """<p>CDMA system ID (SID).</p>"""
    network_id: "aws_sdk_iot_wireless.types.network_id.NetworkId"
    """<p>CDMA network ID (NID).</p>"""
    base_station_id: "aws_sdk_iot_wireless.types.base_station_id.BaseStationId"
    """<p>CDMA base station ID (BSID).</p>"""
    registration_zone: NotRequired[
        "aws_sdk_iot_wireless.types.registration_zone.RegistrationZone"
    ]
    """<p>CDMA registration zone (RZ).</p>"""
    cdma_local_id: NotRequired["aws_sdk_iot_wireless.types.cdma_local_id.CdmaLocalId"]
    """<p>CDMA local identification (local ID) parameters.</p>"""
    pilot_power: NotRequired["aws_sdk_iot_wireless.types.pilot_power.PilotPower"]
    """<p>Transmit power level of the pilot signal, measured in dBm (decibel-milliwatts).</p>"""
    base_lat: NotRequired["aws_sdk_iot_wireless.types.base_lat.BaseLat"]
    """<p>CDMA base station latitude in degrees.</p>"""
    base_lng: NotRequired["aws_sdk_iot_wireless.types.base_lng.BaseLng"]
    """<p>CDMA base station longitude in degrees.</p>"""
    cdma_nmr: NotRequired["aws_sdk_iot_wireless.types.cdma_nmr_list.CdmaNmrList"]
    """<p>CDMA network measurement reports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CdmaObj) -> dict:
    out: dict = {}
    out["SystemId"] = value["system_id"]
    out["NetworkId"] = value["network_id"]
    out["BaseStationId"] = value["base_station_id"]
    if "registration_zone" in value:
        out["RegistrationZone"] = value["registration_zone"]
    if "cdma_local_id" in value:
        import aws_sdk_iot_wireless.types.cdma_local_id

        out["CdmaLocalId"] = aws_sdk_iot_wireless.types.cdma_local_id.serialize_json(
            value["cdma_local_id"]
        )
    if "pilot_power" in value:
        out["PilotPower"] = value["pilot_power"]
    if "base_lat" in value:
        out["BaseLat"] = value["base_lat"]
    if "base_lng" in value:
        out["BaseLng"] = value["base_lng"]
    if "cdma_nmr" in value:
        import aws_sdk_iot_wireless.types.cdma_nmr_list

        out["CdmaNmr"] = aws_sdk_iot_wireless.types.cdma_nmr_list.serialize_json(
            value["cdma_nmr"]
        )
    return out


def deserialize_json(data: dict) -> CdmaObj:
    out: CdmaObj = {}  # type: ignore[typeddict-item]
    if "SystemId" in data:
        out["system_id"] = data["SystemId"]
    else:
        raise DeserializationError("CdmaObj.system_id required")
    if "NetworkId" in data:
        out["network_id"] = data["NetworkId"]
    else:
        raise DeserializationError("CdmaObj.network_id required")
    if "BaseStationId" in data:
        out["base_station_id"] = data["BaseStationId"]
    else:
        raise DeserializationError("CdmaObj.base_station_id required")
    if "RegistrationZone" in data:
        out["registration_zone"] = data["RegistrationZone"]
    if "CdmaLocalId" in data:
        import aws_sdk_iot_wireless.types.cdma_local_id

        out["cdma_local_id"] = (
            aws_sdk_iot_wireless.types.cdma_local_id.deserialize_json(
                data["CdmaLocalId"]
            )
        )
    if "PilotPower" in data:
        out["pilot_power"] = data["PilotPower"]
    if "BaseLat" in data:
        out["base_lat"] = data["BaseLat"]
    if "BaseLng" in data:
        out["base_lng"] = data["BaseLng"]
    if "CdmaNmr" in data:
        import aws_sdk_iot_wireless.types.cdma_nmr_list

        out["cdma_nmr"] = aws_sdk_iot_wireless.types.cdma_nmr_list.deserialize_json(
            data["CdmaNmr"]
        )
    return out
