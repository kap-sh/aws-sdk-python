"""Generated from Smithy shape ``com.amazonaws.medialive#NielsenNaesIiNw``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__double_min1_max65535
    import capo_medialive.types.__string_min2_max2
    import capo_medialive.types.nielsen_watermark_timezones


class NielsenNaesIiNw(TypedDict, closed=True):
    check_digit_string: NotRequired[
        "capo_medialive.types.__string_min2_max2.__stringMin2Max2"
    ]
    """Enter the check digit string for the watermark"""
    sid: NotRequired["capo_medialive.types.__double_min1_max65535.__doubleMin1Max65535"]
    """Enter the Nielsen Source ID (SID) to include in the watermark"""
    timezone: NotRequired[
        "capo_medialive.types.nielsen_watermark_timezones.NielsenWatermarkTimezones"
    ]
    """Choose the timezone for the time stamps in the watermark. If not provided, the timestamps will be in Coordinated Universal Time (UTC)"""


# --- restJson1 ser/de ---
def serialize_json(value: NielsenNaesIiNw) -> dict:
    out: dict = {}
    if "check_digit_string" in value:
        out["checkDigitString"] = value["check_digit_string"]
    if "sid" in value:
        out["sid"] = value["sid"]
    if "timezone" in value:
        import capo_medialive.types.nielsen_watermark_timezones

        out["timezone"] = (
            capo_medialive.types.nielsen_watermark_timezones.serialize_json(
                value["timezone"]
            )
        )
    return out


def deserialize_json(data: dict) -> NielsenNaesIiNw:
    out: NielsenNaesIiNw = {}  # type: ignore[typeddict-item]
    if "checkDigitString" in data:
        out["check_digit_string"] = data["checkDigitString"]
    if "sid" in data:
        out["sid"] = data["sid"]
    if "timezone" in data:
        import capo_medialive.types.nielsen_watermark_timezones

        out["timezone"] = (
            capo_medialive.types.nielsen_watermark_timezones.deserialize_json(
                data["timezone"]
            )
        )
    return out
