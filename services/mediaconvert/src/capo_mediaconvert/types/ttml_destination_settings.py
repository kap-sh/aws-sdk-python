"""Generated from Smithy shape ``com.amazonaws.mediaconvert#TtmlDestinationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.ttml_style_passthrough


class TtmlDestinationSettings(TypedDict, closed=True):
    style_passthrough: NotRequired[
        "capo_mediaconvert.types.ttml_style_passthrough.TtmlStylePassthrough"
    ]
    """Pass through style and position information from a TTML-like input source (TTML, IMSC, SMPTE-TT) to the TTML output."""


# --- restJson1 ser/de ---
def serialize_json(value: TtmlDestinationSettings) -> dict:
    out: dict = {}
    if "style_passthrough" in value:
        import capo_mediaconvert.types.ttml_style_passthrough

        out["stylePassthrough"] = (
            capo_mediaconvert.types.ttml_style_passthrough.serialize_json(
                value["style_passthrough"]
            )
        )
    return out


def deserialize_json(data: dict) -> TtmlDestinationSettings:
    out: TtmlDestinationSettings = {}  # type: ignore[typeddict-item]
    if "stylePassthrough" in data:
        import capo_mediaconvert.types.ttml_style_passthrough

        out["style_passthrough"] = (
            capo_mediaconvert.types.ttml_style_passthrough.deserialize_json(
                data["stylePassthrough"]
            )
        )
    return out
