"""Generated from Smithy shape ``com.amazonaws.mediaconvert#F4vSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.f4v_moov_placement


class F4vSettings(TypedDict, closed=True):
    moov_placement: NotRequired[
        "aws_sdk_mediaconvert.types.f4v_moov_placement.F4vMoovPlacement"
    ]
    """To place the MOOV atom at the beginning of your output, which is useful for progressive downloading: Leave blank or choose Progressive download. To place the MOOV at the end of your output: Choose Normal."""


# --- restJson1 ser/de ---
def serialize_json(value: F4vSettings) -> dict:
    out: dict = {}
    if "moov_placement" in value:
        import aws_sdk_mediaconvert.types.f4v_moov_placement

        out["moovPlacement"] = (
            aws_sdk_mediaconvert.types.f4v_moov_placement.serialize_json(
                value["moov_placement"]
            )
        )
    return out


def deserialize_json(data: dict) -> F4vSettings:
    out: F4vSettings = {}  # type: ignore[typeddict-item]
    if "moovPlacement" in data:
        import aws_sdk_mediaconvert.types.f4v_moov_placement

        out["moov_placement"] = (
            aws_sdk_mediaconvert.types.f4v_moov_placement.deserialize_json(
                data["moovPlacement"]
            )
        )
    return out
