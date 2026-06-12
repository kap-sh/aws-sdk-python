"""Generated from Smithy shape ``com.amazonaws.medialive#Hdr10Settings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer_min0_max32768


class Hdr10Settings(TypedDict):
    max_cll: NotRequired[
        "aws_sdk_medialive.types.__integer_min0_max32768.__integerMin0Max32768"
    ]
    """Maximum Content Light Level An integer metadata value defining the maximum light level, in nits, of any single pixel within an encoded HDR video stream or file."""
    max_fall: NotRequired[
        "aws_sdk_medialive.types.__integer_min0_max32768.__integerMin0Max32768"
    ]
    """Maximum Frame Average Light Level An integer metadata value defining the maximum average light level, in nits, for any single frame within an encoded HDR video stream or file."""


# --- restJson1 ser/de ---
def serialize_json(value: Hdr10Settings) -> dict:
    out: dict = {}
    if "max_cll" in value:
        out["maxCll"] = value["max_cll"]
    if "max_fall" in value:
        out["maxFall"] = value["max_fall"]
    return out


def deserialize_json(data: dict) -> Hdr10Settings:
    out: Hdr10Settings = {}  # type: ignore[typeddict-item]
    if "maxCll" in data:
        out["max_cll"] = data["maxCll"]
    if "maxFall" in data:
        out["max_fall"] = data["maxFall"]
    return out
