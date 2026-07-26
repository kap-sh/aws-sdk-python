"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#Matches``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.match

Matches: TypeAlias = list["capo_codeguruprofiler.types.match.Match"]


# --- restJson1 ser/de ---
def serialize_json(value: Matches) -> list:
    import capo_codeguruprofiler.types.match

    out: list = []
    for item in value:
        out.append(capo_codeguruprofiler.types.match.serialize_json(item))
    return out


def deserialize_json(data: list) -> Matches:
    import capo_codeguruprofiler.types.match

    out: Matches = []
    for item in data:
        out.append(capo_codeguruprofiler.types.match.deserialize_json(item))
    return out
