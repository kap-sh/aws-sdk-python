"""Generated from Smithy shape ``com.amazonaws.iotwireless#TdscdmaObj``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.lac
    import aws_sdk_iot_wireless.types.mcc
    import aws_sdk_iot_wireless.types.mnc
    import aws_sdk_iot_wireless.types.path_loss
    import aws_sdk_iot_wireless.types.rscp
    import aws_sdk_iot_wireless.types.tdscdma_local_id
    import aws_sdk_iot_wireless.types.tdscdma_nmr_list
    import aws_sdk_iot_wireless.types.tdscdma_timing_advance
    import aws_sdk_iot_wireless.types.utran_cid


class TdscdmaObj(TypedDict):
    mcc: "aws_sdk_iot_wireless.types.mcc.MCC"
    """<p>Mobile Country Code.</p>"""
    mnc: "aws_sdk_iot_wireless.types.mnc.MNC"
    """<p>Mobile Network Code.</p>"""
    lac: NotRequired["aws_sdk_iot_wireless.types.lac.LAC"]
    """<p>Location Area Code.</p>"""
    utran_cid: "aws_sdk_iot_wireless.types.utran_cid.UtranCid"
    """<p>UTRAN (UMTS Terrestrial Radio Access Network) Cell Global Identifier.</p>"""
    tdscdma_local_id: NotRequired[
        "aws_sdk_iot_wireless.types.tdscdma_local_id.TdscdmaLocalId"
    ]
    """<p>TD-SCDMA local identification (local ID) information.</p>"""
    tdscdma_timing_advance: NotRequired[
        "aws_sdk_iot_wireless.types.tdscdma_timing_advance.TdscdmaTimingAdvance"
    ]
    """<p>TD-SCDMA Timing advance.</p>"""
    rscp: NotRequired["aws_sdk_iot_wireless.types.rscp.RSCP"]
    """<p>Signal power of the received signal (Received Signal Code Power), measured in decibel-milliwatts (dBm).</p>"""
    path_loss: NotRequired["aws_sdk_iot_wireless.types.path_loss.PathLoss"]
    """<p>Path loss, or path attenuation, is the reduction in power density of an electromagnetic wave as it propagates through space.</p>"""
    tdscdma_nmr: NotRequired[
        "aws_sdk_iot_wireless.types.tdscdma_nmr_list.TdscdmaNmrList"
    ]
    """<p>TD-SCDMA object for network measurement reports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TdscdmaObj) -> dict:
    out: dict = {}
    out["Mcc"] = value["mcc"]
    out["Mnc"] = value["mnc"]
    if "lac" in value:
        out["Lac"] = value["lac"]
    out["UtranCid"] = value["utran_cid"]
    if "tdscdma_local_id" in value:
        import aws_sdk_iot_wireless.types.tdscdma_local_id

        out["TdscdmaLocalId"] = (
            aws_sdk_iot_wireless.types.tdscdma_local_id.serialize_json(
                value["tdscdma_local_id"]
            )
        )
    if "tdscdma_timing_advance" in value:
        out["TdscdmaTimingAdvance"] = value["tdscdma_timing_advance"]
    if "rscp" in value:
        out["Rscp"] = value["rscp"]
    if "path_loss" in value:
        out["PathLoss"] = value["path_loss"]
    if "tdscdma_nmr" in value:
        import aws_sdk_iot_wireless.types.tdscdma_nmr_list

        out["TdscdmaNmr"] = aws_sdk_iot_wireless.types.tdscdma_nmr_list.serialize_json(
            value["tdscdma_nmr"]
        )
    return out


def deserialize_json(data: dict) -> TdscdmaObj:
    out: TdscdmaObj = {}  # type: ignore[typeddict-item]
    if "Mcc" in data:
        out["mcc"] = data["Mcc"]
    else:
        raise DeserializationError("TdscdmaObj.mcc required")
    if "Mnc" in data:
        out["mnc"] = data["Mnc"]
    else:
        raise DeserializationError("TdscdmaObj.mnc required")
    if "Lac" in data:
        out["lac"] = data["Lac"]
    if "UtranCid" in data:
        out["utran_cid"] = data["UtranCid"]
    else:
        raise DeserializationError("TdscdmaObj.utran_cid required")
    if "TdscdmaLocalId" in data:
        import aws_sdk_iot_wireless.types.tdscdma_local_id

        out["tdscdma_local_id"] = (
            aws_sdk_iot_wireless.types.tdscdma_local_id.deserialize_json(
                data["TdscdmaLocalId"]
            )
        )
    if "TdscdmaTimingAdvance" in data:
        out["tdscdma_timing_advance"] = data["TdscdmaTimingAdvance"]
    if "Rscp" in data:
        out["rscp"] = data["Rscp"]
    if "PathLoss" in data:
        out["path_loss"] = data["PathLoss"]
    if "TdscdmaNmr" in data:
        import aws_sdk_iot_wireless.types.tdscdma_nmr_list

        out["tdscdma_nmr"] = (
            aws_sdk_iot_wireless.types.tdscdma_nmr_list.deserialize_json(
                data["TdscdmaNmr"]
            )
        )
    return out
