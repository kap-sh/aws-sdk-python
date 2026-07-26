"""Generated from Smithy shape ``com.amazonaws.controltower#LandingZoneSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.arn


class LandingZoneSummary(TypedDict, closed=True):
    arn: NotRequired["capo_controltower.types.arn.Arn"]
    """<p>The ARN of the landing zone.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LandingZoneSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> LandingZoneSummary:
    out: LandingZoneSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
