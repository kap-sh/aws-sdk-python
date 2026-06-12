"""Generated from Smithy shape ``com.amazonaws.iotwireless#SessionKeysAbpV1_0_x``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.app_s_key
    import aws_sdk_iot_wireless.types.nwk_s_key


class SessionKeysAbpV1_0_x(TypedDict):
    nwk_s_key: NotRequired["aws_sdk_iot_wireless.types.nwk_s_key.NwkSKey"]
    """<p>The NwkSKey value.</p>"""
    app_s_key: NotRequired["aws_sdk_iot_wireless.types.app_s_key.AppSKey"]
    """<p>The AppSKey value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionKeysAbpV1_0_x) -> dict:
    out: dict = {}
    if "nwk_s_key" in value:
        out["NwkSKey"] = value["nwk_s_key"]
    if "app_s_key" in value:
        out["AppSKey"] = value["app_s_key"]
    return out


def deserialize_json(data: dict) -> SessionKeysAbpV1_0_x:
    out: SessionKeysAbpV1_0_x = {}  # type: ignore[typeddict-item]
    if "NwkSKey" in data:
        out["nwk_s_key"] = data["NwkSKey"]
    if "AppSKey" in data:
        out["app_s_key"] = data["AppSKey"]
    return out
