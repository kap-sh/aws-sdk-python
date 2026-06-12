"""Generated from Smithy shape ``com.amazonaws.iotwireless#UpdateAbpV1_1``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.f_cnt_start


class UpdateAbpV1_1(TypedDict):
    f_cnt_start: NotRequired["aws_sdk_iot_wireless.types.f_cnt_start.FCntStart"]
    """<p>The FCnt init value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAbpV1_1) -> dict:
    out: dict = {}
    if "f_cnt_start" in value:
        out["FCntStart"] = value["f_cnt_start"]
    return out


def deserialize_json(data: dict) -> UpdateAbpV1_1:
    out: UpdateAbpV1_1 = {}  # type: ignore[typeddict-item]
    if "FCntStart" in data:
        out["f_cnt_start"] = data["FCntStart"]
    return out
