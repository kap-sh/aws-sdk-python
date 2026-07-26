"""Generated from Smithy shape ``com.amazonaws.medialive#MediaResourceNeighbor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string_min1_max256
    import capo_medialive.types.__string_min1_max2048_pattern_arn


class MediaResourceNeighbor(TypedDict, closed=True):
    arn: NotRequired[
        "capo_medialive.types.__string_min1_max2048_pattern_arn.__stringMin1Max2048PatternArn"
    ]
    """The ARN of a resource used in AWS media workflows."""
    name: NotRequired["capo_medialive.types.__string_min1_max256.__stringMin1Max256"]
    """The logical name of an AWS media resource."""


# --- restJson1 ser/de ---
def serialize_json(value: MediaResourceNeighbor) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> MediaResourceNeighbor:
    out: MediaResourceNeighbor = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    return out
