"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DvbSubSourceSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min1_max2147483647


class DvbSubSourceSettings(TypedDict):
    pid: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
    ]
    """When using DVB-Sub with Burn-in, use this PID for the source content. Unused for DVB-Sub passthrough. All DVB-Sub content is passed through, regardless of selectors."""


# --- restJson1 ser/de ---
def serialize_json(value: DvbSubSourceSettings) -> dict:
    out: dict = {}
    if "pid" in value:
        out["pid"] = value["pid"]
    return out


def deserialize_json(data: dict) -> DvbSubSourceSettings:
    out: DvbSubSourceSettings = {}  # type: ignore[typeddict-item]
    if "pid" in data:
        out["pid"] = data["pid"]
    return out
