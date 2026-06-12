"""Generated from Smithy shape ``com.amazonaws.iotwireless#CellTowers``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.cdma_list
    import aws_sdk_iot_wireless.types.gsm_list
    import aws_sdk_iot_wireless.types.lte_list
    import aws_sdk_iot_wireless.types.tdscdma_list
    import aws_sdk_iot_wireless.types.wcdma_list


class CellTowers(TypedDict):
    gsm: NotRequired["aws_sdk_iot_wireless.types.gsm_list.GsmList"]
    """<p>GSM object information.</p>"""
    wcdma: NotRequired["aws_sdk_iot_wireless.types.wcdma_list.WcdmaList"]
    """<p>WCDMA object information.</p>"""
    tdscdma: NotRequired["aws_sdk_iot_wireless.types.tdscdma_list.TdscdmaList"]
    """<p>TD-SCDMA object information.</p>"""
    lte: NotRequired["aws_sdk_iot_wireless.types.lte_list.LteList"]
    """<p>LTE object information.</p>"""
    cdma: NotRequired["aws_sdk_iot_wireless.types.cdma_list.CdmaList"]
    """<p>CDMA object information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CellTowers) -> dict:
    out: dict = {}
    if "gsm" in value:
        import aws_sdk_iot_wireless.types.gsm_list

        out["Gsm"] = aws_sdk_iot_wireless.types.gsm_list.serialize_json(value["gsm"])
    if "wcdma" in value:
        import aws_sdk_iot_wireless.types.wcdma_list

        out["Wcdma"] = aws_sdk_iot_wireless.types.wcdma_list.serialize_json(
            value["wcdma"]
        )
    if "tdscdma" in value:
        import aws_sdk_iot_wireless.types.tdscdma_list

        out["Tdscdma"] = aws_sdk_iot_wireless.types.tdscdma_list.serialize_json(
            value["tdscdma"]
        )
    if "lte" in value:
        import aws_sdk_iot_wireless.types.lte_list

        out["Lte"] = aws_sdk_iot_wireless.types.lte_list.serialize_json(value["lte"])
    if "cdma" in value:
        import aws_sdk_iot_wireless.types.cdma_list

        out["Cdma"] = aws_sdk_iot_wireless.types.cdma_list.serialize_json(value["cdma"])
    return out


def deserialize_json(data: dict) -> CellTowers:
    out: CellTowers = {}  # type: ignore[typeddict-item]
    if "Gsm" in data:
        import aws_sdk_iot_wireless.types.gsm_list

        out["gsm"] = aws_sdk_iot_wireless.types.gsm_list.deserialize_json(data["Gsm"])
    if "Wcdma" in data:
        import aws_sdk_iot_wireless.types.wcdma_list

        out["wcdma"] = aws_sdk_iot_wireless.types.wcdma_list.deserialize_json(
            data["Wcdma"]
        )
    if "Tdscdma" in data:
        import aws_sdk_iot_wireless.types.tdscdma_list

        out["tdscdma"] = aws_sdk_iot_wireless.types.tdscdma_list.deserialize_json(
            data["Tdscdma"]
        )
    if "Lte" in data:
        import aws_sdk_iot_wireless.types.lte_list

        out["lte"] = aws_sdk_iot_wireless.types.lte_list.deserialize_json(data["Lte"])
    if "Cdma" in data:
        import aws_sdk_iot_wireless.types.cdma_list

        out["cdma"] = aws_sdk_iot_wireless.types.cdma_list.deserialize_json(
            data["Cdma"]
        )
    return out
