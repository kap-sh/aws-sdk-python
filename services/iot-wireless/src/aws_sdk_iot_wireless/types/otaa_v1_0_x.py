"""Generated from Smithy shape ``com.amazonaws.iotwireless#OtaaV1_0_x``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.app_eui
    import aws_sdk_iot_wireless.types.app_key
    import aws_sdk_iot_wireless.types.gen_app_key
    import aws_sdk_iot_wireless.types.join_eui


class OtaaV1_0_x(TypedDict, closed=True):
    app_key: NotRequired["aws_sdk_iot_wireless.types.app_key.AppKey"]
    """<p>The AppKey value.</p>"""
    app_eui: NotRequired["aws_sdk_iot_wireless.types.app_eui.AppEui"]
    """<p>The AppEUI value. You specify this value when using LoRaWAN versions v1.0.2 or v1.0.3.</p>"""
    join_eui: NotRequired["aws_sdk_iot_wireless.types.join_eui.JoinEui"]
    """<p>The JoinEUI value. You specify this value instead of the AppEUI when using LoRaWAN version v1.0.4.</p>"""
    gen_app_key: NotRequired["aws_sdk_iot_wireless.types.gen_app_key.GenAppKey"]
    """<p>The GenAppKey value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OtaaV1_0_x) -> dict:
    out: dict = {}
    if "app_key" in value:
        out["AppKey"] = value["app_key"]
    if "app_eui" in value:
        out["AppEui"] = value["app_eui"]
    if "join_eui" in value:
        out["JoinEui"] = value["join_eui"]
    if "gen_app_key" in value:
        out["GenAppKey"] = value["gen_app_key"]
    return out


def deserialize_json(data: dict) -> OtaaV1_0_x:
    out: OtaaV1_0_x = {}  # type: ignore[typeddict-item]
    if "AppKey" in data:
        out["app_key"] = data["AppKey"]
    if "AppEui" in data:
        out["app_eui"] = data["AppEui"]
    if "JoinEui" in data:
        out["join_eui"] = data["JoinEui"]
    if "GenAppKey" in data:
        out["gen_app_key"] = data["GenAppKey"]
    return out
