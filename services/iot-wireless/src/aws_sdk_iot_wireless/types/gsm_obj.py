"""Generated from Smithy shape ``com.amazonaws.iotwireless#GsmObj``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.geran_cid
    import aws_sdk_iot_wireless.types.gsm_local_id
    import aws_sdk_iot_wireless.types.gsm_nmr_list
    import aws_sdk_iot_wireless.types.gsm_timing_advance
    import aws_sdk_iot_wireless.types.lac
    import aws_sdk_iot_wireless.types.mcc
    import aws_sdk_iot_wireless.types.mnc
    import aws_sdk_iot_wireless.types.rx_level


class GsmObj(TypedDict, closed=True):
    mcc: "aws_sdk_iot_wireless.types.mcc.MCC"
    """<p>Mobile Country Code.</p>"""
    mnc: "aws_sdk_iot_wireless.types.mnc.MNC"
    """<p>Mobile Network Code.</p>"""
    lac: "aws_sdk_iot_wireless.types.lac.LAC"
    """<p>Location area code.</p>"""
    geran_cid: "aws_sdk_iot_wireless.types.geran_cid.GeranCid"
    """<p>GERAN (GSM EDGE Radio Access Network) Cell Global Identifier.</p>"""
    gsm_local_id: NotRequired["aws_sdk_iot_wireless.types.gsm_local_id.GsmLocalId"]
    """<p>GSM local identification (local ID) information.</p>"""
    gsm_timing_advance: NotRequired[
        "aws_sdk_iot_wireless.types.gsm_timing_advance.GsmTimingAdvance"
    ]
    """<p>Timing advance value, which corresponds to the length of time a signal takes to reach the base station from a mobile phone.</p>"""
    rx_level: NotRequired["aws_sdk_iot_wireless.types.rx_level.RxLevel"]
    """<p>Rx level, which is the received signal power, measured in dBm (decibel-milliwatts).</p>"""
    gsm_nmr: NotRequired["aws_sdk_iot_wireless.types.gsm_nmr_list.GsmNmrList"]
    """<p>GSM object for network measurement reports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GsmObj) -> dict:
    out: dict = {}
    out["Mcc"] = value["mcc"]
    out["Mnc"] = value["mnc"]
    out["Lac"] = value["lac"]
    out["GeranCid"] = value["geran_cid"]
    if "gsm_local_id" in value:
        import aws_sdk_iot_wireless.types.gsm_local_id

        out["GsmLocalId"] = aws_sdk_iot_wireless.types.gsm_local_id.serialize_json(
            value["gsm_local_id"]
        )
    if "gsm_timing_advance" in value:
        out["GsmTimingAdvance"] = value["gsm_timing_advance"]
    if "rx_level" in value:
        out["RxLevel"] = value["rx_level"]
    if "gsm_nmr" in value:
        import aws_sdk_iot_wireless.types.gsm_nmr_list

        out["GsmNmr"] = aws_sdk_iot_wireless.types.gsm_nmr_list.serialize_json(
            value["gsm_nmr"]
        )
    return out


def deserialize_json(data: dict) -> GsmObj:
    out: GsmObj = {}  # type: ignore[typeddict-item]
    if "Mcc" in data:
        out["mcc"] = data["Mcc"]
    else:
        raise DeserializationError("GsmObj.mcc required")
    if "Mnc" in data:
        out["mnc"] = data["Mnc"]
    else:
        raise DeserializationError("GsmObj.mnc required")
    if "Lac" in data:
        out["lac"] = data["Lac"]
    else:
        raise DeserializationError("GsmObj.lac required")
    if "GeranCid" in data:
        out["geran_cid"] = data["GeranCid"]
    else:
        raise DeserializationError("GsmObj.geran_cid required")
    if "GsmLocalId" in data:
        import aws_sdk_iot_wireless.types.gsm_local_id

        out["gsm_local_id"] = aws_sdk_iot_wireless.types.gsm_local_id.deserialize_json(
            data["GsmLocalId"]
        )
    if "GsmTimingAdvance" in data:
        out["gsm_timing_advance"] = data["GsmTimingAdvance"]
    if "RxLevel" in data:
        out["rx_level"] = data["RxLevel"]
    if "GsmNmr" in data:
        import aws_sdk_iot_wireless.types.gsm_nmr_list

        out["gsm_nmr"] = aws_sdk_iot_wireless.types.gsm_nmr_list.deserialize_json(
            data["GsmNmr"]
        )
    return out
