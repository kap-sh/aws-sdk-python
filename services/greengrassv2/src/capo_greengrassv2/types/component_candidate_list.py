"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ComponentCandidateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrassv2.types.component_candidate

ComponentCandidateList: TypeAlias = list[
    "capo_greengrassv2.types.component_candidate.ComponentCandidate"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentCandidateList) -> list:
    import capo_greengrassv2.types.component_candidate

    out: list = []
    for item in value:
        out.append(capo_greengrassv2.types.component_candidate.serialize_json(item))
    return out


def deserialize_json(data: list) -> ComponentCandidateList:
    import capo_greengrassv2.types.component_candidate

    out: ComponentCandidateList = []
    for item in data:
        out.append(capo_greengrassv2.types.component_candidate.deserialize_json(item))
    return out
