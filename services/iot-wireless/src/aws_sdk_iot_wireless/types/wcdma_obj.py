"""Generated from Smithy shape ``com.amazonaws.iotwireless#WcdmaObj``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.lac
    import aws_sdk_iot_wireless.types.mcc
    import aws_sdk_iot_wireless.types.mnc
    import aws_sdk_iot_wireless.types.path_loss
    import aws_sdk_iot_wireless.types.rscp
    import aws_sdk_iot_wireless.types.utran_cid
    import aws_sdk_iot_wireless.types.wcdma_local_id
    import aws_sdk_iot_wireless.types.wcdma_nmr_list


class WcdmaObj(TypedDict, closed=True):
    mcc: "aws_sdk_iot_wireless.types.mcc.MCC"
    """<p>Mobile Country Code.</p>"""
    mnc: "aws_sdk_iot_wireless.types.mnc.MNC"
    """<p>Mobile Network Code.</p>"""
    lac: NotRequired["aws_sdk_iot_wireless.types.lac.LAC"]
    """<p>Location Area Code.</p>"""
    utran_cid: "aws_sdk_iot_wireless.types.utran_cid.UtranCid"
    """<p>UTRAN (UMTS Terrestrial Radio Access Network) Cell Global Identifier.</p>"""
    wcdma_local_id: NotRequired[
        "aws_sdk_iot_wireless.types.wcdma_local_id.WcdmaLocalId"
    ]
    """<p>WCDMA local ID information.</p>"""
    rscp: NotRequired["aws_sdk_iot_wireless.types.rscp.RSCP"]
    """<p>Received Signal Code Power (signal power) (dBm).</p>"""
    path_loss: NotRequired["aws_sdk_iot_wireless.types.path_loss.PathLoss"]
    """<p>Path loss, or path attenuation, is the reduction in power density of an electromagnetic wave as it propagates through space.</p>"""
    wcdma_nmr: NotRequired["aws_sdk_iot_wireless.types.wcdma_nmr_list.WcdmaNmrList"]
    """<p>WCDMA object for network measurement reports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WcdmaObj) -> dict:
    out: dict = {}
    out["Mcc"] = value["mcc"]
    out["Mnc"] = value["mnc"]
    if "lac" in value:
        out["Lac"] = value["lac"]
    out["UtranCid"] = value["utran_cid"]
    if "wcdma_local_id" in value:
        import aws_sdk_iot_wireless.types.wcdma_local_id

        out["WcdmaLocalId"] = aws_sdk_iot_wireless.types.wcdma_local_id.serialize_json(
            value["wcdma_local_id"]
        )
    if "rscp" in value:
        out["Rscp"] = value["rscp"]
    if "path_loss" in value:
        out["PathLoss"] = value["path_loss"]
    if "wcdma_nmr" in value:
        import aws_sdk_iot_wireless.types.wcdma_nmr_list

        out["WcdmaNmr"] = aws_sdk_iot_wireless.types.wcdma_nmr_list.serialize_json(
            value["wcdma_nmr"]
        )
    return out


def deserialize_json(data: dict) -> WcdmaObj:
    out: WcdmaObj = {}  # type: ignore[typeddict-item]
    if "Mcc" in data:
        out["mcc"] = data["Mcc"]
    else:
        raise DeserializationError("WcdmaObj.mcc required")
    if "Mnc" in data:
        out["mnc"] = data["Mnc"]
    else:
        raise DeserializationError("WcdmaObj.mnc required")
    if "Lac" in data:
        out["lac"] = data["Lac"]
    if "UtranCid" in data:
        out["utran_cid"] = data["UtranCid"]
    else:
        raise DeserializationError("WcdmaObj.utran_cid required")
    if "WcdmaLocalId" in data:
        import aws_sdk_iot_wireless.types.wcdma_local_id

        out["wcdma_local_id"] = (
            aws_sdk_iot_wireless.types.wcdma_local_id.deserialize_json(
                data["WcdmaLocalId"]
            )
        )
    if "Rscp" in data:
        out["rscp"] = data["Rscp"]
    if "PathLoss" in data:
        out["path_loss"] = data["PathLoss"]
    if "WcdmaNmr" in data:
        import aws_sdk_iot_wireless.types.wcdma_nmr_list

        out["wcdma_nmr"] = aws_sdk_iot_wireless.types.wcdma_nmr_list.deserialize_json(
            data["WcdmaNmr"]
        )
    return out
