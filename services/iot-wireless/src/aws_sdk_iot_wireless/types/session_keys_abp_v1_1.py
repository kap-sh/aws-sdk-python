"""Generated from Smithy shape ``com.amazonaws.iotwireless#SessionKeysAbpV1_1``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.app_s_key
    import aws_sdk_iot_wireless.types.f_nwk_s_int_key
    import aws_sdk_iot_wireless.types.nwk_s_enc_key
    import aws_sdk_iot_wireless.types.s_nwk_s_int_key


class SessionKeysAbpV1_1(TypedDict):
    f_nwk_s_int_key: NotRequired[
        "aws_sdk_iot_wireless.types.f_nwk_s_int_key.FNwkSIntKey"
    ]
    """<p>The FNwkSIntKey value.</p>"""
    s_nwk_s_int_key: NotRequired[
        "aws_sdk_iot_wireless.types.s_nwk_s_int_key.SNwkSIntKey"
    ]
    """<p>The SNwkSIntKey value.</p>"""
    nwk_s_enc_key: NotRequired["aws_sdk_iot_wireless.types.nwk_s_enc_key.NwkSEncKey"]
    """<p>The NwkSEncKey value.</p>"""
    app_s_key: NotRequired["aws_sdk_iot_wireless.types.app_s_key.AppSKey"]
    """<p>The AppSKey value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionKeysAbpV1_1) -> dict:
    out: dict = {}
    if "f_nwk_s_int_key" in value:
        out["FNwkSIntKey"] = value["f_nwk_s_int_key"]
    if "s_nwk_s_int_key" in value:
        out["SNwkSIntKey"] = value["s_nwk_s_int_key"]
    if "nwk_s_enc_key" in value:
        out["NwkSEncKey"] = value["nwk_s_enc_key"]
    if "app_s_key" in value:
        out["AppSKey"] = value["app_s_key"]
    return out


def deserialize_json(data: dict) -> SessionKeysAbpV1_1:
    out: SessionKeysAbpV1_1 = {}  # type: ignore[typeddict-item]
    if "FNwkSIntKey" in data:
        out["f_nwk_s_int_key"] = data["FNwkSIntKey"]
    if "SNwkSIntKey" in data:
        out["s_nwk_s_int_key"] = data["SNwkSIntKey"]
    if "NwkSEncKey" in data:
        out["nwk_s_enc_key"] = data["NwkSEncKey"]
    if "AppSKey" in data:
        out["app_s_key"] = data["AppSKey"]
    return out
