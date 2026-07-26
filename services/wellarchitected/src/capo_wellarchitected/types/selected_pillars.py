"""Generated from Smithy shape ``com.amazonaws.wellarchitected#SelectedPillars``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.selected_pillar

SelectedPillars: TypeAlias = list[
    "capo_wellarchitected.types.selected_pillar.SelectedPillar"
]


# --- restJson1 ser/de ---
def serialize_json(value: SelectedPillars) -> list:
    import capo_wellarchitected.types.selected_pillar

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.selected_pillar.serialize_json(item))
    return out


def deserialize_json(data: list) -> SelectedPillars:
    import capo_wellarchitected.types.selected_pillar

    out: SelectedPillars = []
    for item in data:
        out.append(capo_wellarchitected.types.selected_pillar.deserialize_json(item))
    return out
