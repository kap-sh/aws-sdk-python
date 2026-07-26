"""Generated from Smithy shape ``com.amazonaws.iotwireless#CellTowers``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.cdma_list
    import capo_iot_wireless.types.gsm_list
    import capo_iot_wireless.types.lte_list
    import capo_iot_wireless.types.tdscdma_list
    import capo_iot_wireless.types.wcdma_list


class CellTowers(TypedDict, closed=True):
    gsm: NotRequired["capo_iot_wireless.types.gsm_list.GsmList"]
    """<p>GSM object information.</p>"""
    wcdma: NotRequired["capo_iot_wireless.types.wcdma_list.WcdmaList"]
    """<p>WCDMA object information.</p>"""
    tdscdma: NotRequired["capo_iot_wireless.types.tdscdma_list.TdscdmaList"]
    """<p>TD-SCDMA object information.</p>"""
    lte: NotRequired["capo_iot_wireless.types.lte_list.LteList"]
    """<p>LTE object information.</p>"""
    cdma: NotRequired["capo_iot_wireless.types.cdma_list.CdmaList"]
    """<p>CDMA object information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CellTowers) -> dict:
    out: dict = {}
    if "gsm" in value:
        import capo_iot_wireless.types.gsm_list

        out["Gsm"] = capo_iot_wireless.types.gsm_list.serialize_json(value["gsm"])
    if "wcdma" in value:
        import capo_iot_wireless.types.wcdma_list

        out["Wcdma"] = capo_iot_wireless.types.wcdma_list.serialize_json(value["wcdma"])
    if "tdscdma" in value:
        import capo_iot_wireless.types.tdscdma_list

        out["Tdscdma"] = capo_iot_wireless.types.tdscdma_list.serialize_json(
            value["tdscdma"]
        )
    if "lte" in value:
        import capo_iot_wireless.types.lte_list

        out["Lte"] = capo_iot_wireless.types.lte_list.serialize_json(value["lte"])
    if "cdma" in value:
        import capo_iot_wireless.types.cdma_list

        out["Cdma"] = capo_iot_wireless.types.cdma_list.serialize_json(value["cdma"])
    return out


def deserialize_json(data: dict) -> CellTowers:
    out: CellTowers = {}  # type: ignore[typeddict-item]
    if "Gsm" in data:
        import capo_iot_wireless.types.gsm_list

        out["gsm"] = capo_iot_wireless.types.gsm_list.deserialize_json(data["Gsm"])
    if "Wcdma" in data:
        import capo_iot_wireless.types.wcdma_list

        out["wcdma"] = capo_iot_wireless.types.wcdma_list.deserialize_json(
            data["Wcdma"]
        )
    if "Tdscdma" in data:
        import capo_iot_wireless.types.tdscdma_list

        out["tdscdma"] = capo_iot_wireless.types.tdscdma_list.deserialize_json(
            data["Tdscdma"]
        )
    if "Lte" in data:
        import capo_iot_wireless.types.lte_list

        out["lte"] = capo_iot_wireless.types.lte_list.deserialize_json(data["Lte"])
    if "Cdma" in data:
        import capo_iot_wireless.types.cdma_list

        out["cdma"] = capo_iot_wireless.types.cdma_list.deserialize_json(data["Cdma"])
    return out
