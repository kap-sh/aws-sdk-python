"""Generated from Smithy shape ``com.amazonaws.iotwireless#AbpV1_1``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.dev_addr
    import aws_sdk_iot_wireless.types.f_cnt_start
    import aws_sdk_iot_wireless.types.session_keys_abp_v1_1


class AbpV1_1(TypedDict):
    dev_addr: NotRequired["aws_sdk_iot_wireless.types.dev_addr.DevAddr"]
    """<p>The DevAddr value.</p>"""
    session_keys: NotRequired[
        "aws_sdk_iot_wireless.types.session_keys_abp_v1_1.SessionKeysAbpV1_1"
    ]
    """<p>Session keys for ABP v1.1</p>"""
    f_cnt_start: NotRequired["aws_sdk_iot_wireless.types.f_cnt_start.FCntStart"]
    """<p>The FCnt init value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AbpV1_1) -> dict:
    out: dict = {}
    if "dev_addr" in value:
        out["DevAddr"] = value["dev_addr"]
    if "session_keys" in value:
        import aws_sdk_iot_wireless.types.session_keys_abp_v1_1

        out["SessionKeys"] = (
            aws_sdk_iot_wireless.types.session_keys_abp_v1_1.serialize_json(
                value["session_keys"]
            )
        )
    if "f_cnt_start" in value:
        out["FCntStart"] = value["f_cnt_start"]
    return out


def deserialize_json(data: dict) -> AbpV1_1:
    out: AbpV1_1 = {}  # type: ignore[typeddict-item]
    if "DevAddr" in data:
        out["dev_addr"] = data["DevAddr"]
    if "SessionKeys" in data:
        import aws_sdk_iot_wireless.types.session_keys_abp_v1_1

        out["session_keys"] = (
            aws_sdk_iot_wireless.types.session_keys_abp_v1_1.deserialize_json(
                data["SessionKeys"]
            )
        )
    if "FCntStart" in data:
        out["f_cnt_start"] = data["FCntStart"]
    return out
