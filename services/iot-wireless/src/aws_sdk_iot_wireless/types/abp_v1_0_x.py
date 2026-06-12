"""Generated from Smithy shape ``com.amazonaws.iotwireless#AbpV1_0_x``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.dev_addr
    import aws_sdk_iot_wireless.types.f_cnt_start
    import aws_sdk_iot_wireless.types.session_keys_abp_v1_0_x


class AbpV1_0_x(TypedDict):
    dev_addr: NotRequired["aws_sdk_iot_wireless.types.dev_addr.DevAddr"]
    """<p>The DevAddr value.</p>"""
    session_keys: NotRequired[
        "aws_sdk_iot_wireless.types.session_keys_abp_v1_0_x.SessionKeysAbpV1_0_x"
    ]
    """<p>Session keys for ABP v1.0.x</p>"""
    f_cnt_start: NotRequired["aws_sdk_iot_wireless.types.f_cnt_start.FCntStart"]
    """<p>The FCnt init value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AbpV1_0_x) -> dict:
    out: dict = {}
    if "dev_addr" in value:
        out["DevAddr"] = value["dev_addr"]
    if "session_keys" in value:
        import aws_sdk_iot_wireless.types.session_keys_abp_v1_0_x

        out["SessionKeys"] = (
            aws_sdk_iot_wireless.types.session_keys_abp_v1_0_x.serialize_json(
                value["session_keys"]
            )
        )
    if "f_cnt_start" in value:
        out["FCntStart"] = value["f_cnt_start"]
    return out


def deserialize_json(data: dict) -> AbpV1_0_x:
    out: AbpV1_0_x = {}  # type: ignore[typeddict-item]
    if "DevAddr" in data:
        out["dev_addr"] = data["DevAddr"]
    if "SessionKeys" in data:
        import aws_sdk_iot_wireless.types.session_keys_abp_v1_0_x

        out["session_keys"] = (
            aws_sdk_iot_wireless.types.session_keys_abp_v1_0_x.deserialize_json(
                data["SessionKeys"]
            )
        )
    if "FCntStart" in data:
        out["f_cnt_start"] = data["FCntStart"]
    return out
