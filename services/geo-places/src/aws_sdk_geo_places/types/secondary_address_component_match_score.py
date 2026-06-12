"""Generated from Smithy shape ``com.amazonaws.geoplaces#SecondaryAddressComponentMatchScore``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.match_score


class SecondaryAddressComponentMatchScore(TypedDict):
    number: "aws_sdk_geo_places.types.match_score.MatchScore"
    """<p>Match score for the secondary address number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecondaryAddressComponentMatchScore) -> dict:
    out: dict = {}
    out["Number"] = value.get("number", 0)
    return out


def deserialize_json(data: dict) -> SecondaryAddressComponentMatchScore:
    out: SecondaryAddressComponentMatchScore = {}  # type: ignore[typeddict-item]
    if "Number" in data:
        out["number"] = data["Number"]
    else:
        out["number"] = 0
    return out
