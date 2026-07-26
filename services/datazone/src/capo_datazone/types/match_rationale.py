"""Generated from Smithy shape ``com.amazonaws.datazone#MatchRationale``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.match_rationale_item

MatchRationale: TypeAlias = list[
    "capo_datazone.types.match_rationale_item.MatchRationaleItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: MatchRationale) -> list:
    import capo_datazone.types.match_rationale_item

    out: list = []
    for item in value:
        out.append(capo_datazone.types.match_rationale_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> MatchRationale:
    import capo_datazone.types.match_rationale_item

    out: MatchRationale = []
    for item in data:
        out.append(capo_datazone.types.match_rationale_item.deserialize_json(item))
    return out
