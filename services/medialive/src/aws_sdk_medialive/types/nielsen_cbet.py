"""Generated from Smithy shape ``com.amazonaws.medialive#NielsenCBET``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string_min1_max7
    import aws_sdk_medialive.types.__string_min2_max2
    import aws_sdk_medialive.types.nielsen_watermarks_cbet_stepaside


class NielsenCBET(TypedDict, closed=True):
    cbet_check_digit_string: NotRequired[
        "aws_sdk_medialive.types.__string_min2_max2.__stringMin2Max2"
    ]
    """Enter the CBET check digits to use in the watermark."""
    cbet_stepaside: NotRequired[
        "aws_sdk_medialive.types.nielsen_watermarks_cbet_stepaside.NielsenWatermarksCbetStepaside"
    ]
    """Determines the method of CBET insertion mode when prior encoding is detected on the same layer."""
    csid: NotRequired["aws_sdk_medialive.types.__string_min1_max7.__stringMin1Max7"]
    """Enter the CBET Source ID (CSID) to use in the watermark"""


# --- restJson1 ser/de ---
def serialize_json(value: NielsenCBET) -> dict:
    out: dict = {}
    if "cbet_check_digit_string" in value:
        out["cbetCheckDigitString"] = value["cbet_check_digit_string"]
    if "cbet_stepaside" in value:
        import aws_sdk_medialive.types.nielsen_watermarks_cbet_stepaside

        out["cbetStepaside"] = (
            aws_sdk_medialive.types.nielsen_watermarks_cbet_stepaside.serialize_json(
                value["cbet_stepaside"]
            )
        )
    if "csid" in value:
        out["csid"] = value["csid"]
    return out


def deserialize_json(data: dict) -> NielsenCBET:
    out: NielsenCBET = {}  # type: ignore[typeddict-item]
    if "cbetCheckDigitString" in data:
        out["cbet_check_digit_string"] = data["cbetCheckDigitString"]
    if "cbetStepaside" in data:
        import aws_sdk_medialive.types.nielsen_watermarks_cbet_stepaside

        out["cbet_stepaside"] = (
            aws_sdk_medialive.types.nielsen_watermarks_cbet_stepaside.deserialize_json(
                data["cbetStepaside"]
            )
        )
    if "csid" in data:
        out["csid"] = data["csid"]
    return out
