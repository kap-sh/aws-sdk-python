"""Generated from Smithy shape ``com.amazonaws.entityresolution#MatchGroupsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_entityresolution.types.match_group

MatchGroupsList: TypeAlias = list["capo_entityresolution.types.match_group.MatchGroup"]


# --- restJson1 ser/de ---
def serialize_json(value: MatchGroupsList) -> list:
    import capo_entityresolution.types.match_group

    out: list = []
    for item in value:
        out.append(capo_entityresolution.types.match_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> MatchGroupsList:
    import capo_entityresolution.types.match_group

    out: MatchGroupsList = []
    for item in data:
        out.append(capo_entityresolution.types.match_group.deserialize_json(item))
    return out
