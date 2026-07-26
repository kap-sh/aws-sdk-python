"""Generated from Smithy shape ``com.amazonaws.geoplaces#MatchScoreList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.match_score

MatchScoreList: TypeAlias = list["capo_geo_places.types.match_score.MatchScore"]


# --- restJson1 ser/de ---
def serialize_json(value: MatchScoreList) -> list:
    return list(value)


def deserialize_json(data: list) -> MatchScoreList:
    return list(data)
