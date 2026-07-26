"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DolbyVisionLevel6Metadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min0_max65535


class DolbyVisionLevel6Metadata(TypedDict, closed=True):
    max_cll: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max65535.__integerMin0Max65535"
    ]
    """Maximum Content Light Level. Static HDR metadata that corresponds to the brightest pixel in the entire stream. Measured in nits."""
    max_fall: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max65535.__integerMin0Max65535"
    ]
    """Maximum Frame-Average Light Level. Static HDR metadata that corresponds to the highest frame-average brightness in the entire stream. Measured in nits."""


# --- restJson1 ser/de ---
def serialize_json(value: DolbyVisionLevel6Metadata) -> dict:
    out: dict = {}
    if "max_cll" in value:
        out["maxCll"] = value["max_cll"]
    if "max_fall" in value:
        out["maxFall"] = value["max_fall"]
    return out


def deserialize_json(data: dict) -> DolbyVisionLevel6Metadata:
    out: DolbyVisionLevel6Metadata = {}  # type: ignore[typeddict-item]
    if "maxCll" in data:
        out["max_cll"] = data["maxCll"]
    if "maxFall" in data:
        out["max_fall"] = data["maxFall"]
    return out
