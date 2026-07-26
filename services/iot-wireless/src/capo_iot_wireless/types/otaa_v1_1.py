"""Generated from Smithy shape ``com.amazonaws.iotwireless#OtaaV1_1``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.app_key
    import capo_iot_wireless.types.join_eui
    import capo_iot_wireless.types.nwk_key


class OtaaV1_1(TypedDict, closed=True):
    app_key: NotRequired["capo_iot_wireless.types.app_key.AppKey"]
    """<p>The AppKey value.</p>"""
    nwk_key: NotRequired["capo_iot_wireless.types.nwk_key.NwkKey"]
    """<p>The NwkKey value.</p>"""
    join_eui: NotRequired["capo_iot_wireless.types.join_eui.JoinEui"]
    """<p>The JoinEUI value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OtaaV1_1) -> dict:
    out: dict = {}
    if "app_key" in value:
        out["AppKey"] = value["app_key"]
    if "nwk_key" in value:
        out["NwkKey"] = value["nwk_key"]
    if "join_eui" in value:
        out["JoinEui"] = value["join_eui"]
    return out


def deserialize_json(data: dict) -> OtaaV1_1:
    out: OtaaV1_1 = {}  # type: ignore[typeddict-item]
    if "AppKey" in data:
        out["app_key"] = data["AppKey"]
    if "NwkKey" in data:
        out["nwk_key"] = data["NwkKey"]
    if "JoinEui" in data:
        out["join_eui"] = data["JoinEui"]
    return out
