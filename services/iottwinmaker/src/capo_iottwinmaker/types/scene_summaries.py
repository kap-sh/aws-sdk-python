"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#SceneSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.scene_summary

SceneSummaries: TypeAlias = list["capo_iottwinmaker.types.scene_summary.SceneSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: SceneSummaries) -> list:
    import capo_iottwinmaker.types.scene_summary

    out: list = []
    for item in value:
        out.append(capo_iottwinmaker.types.scene_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> SceneSummaries:
    import capo_iottwinmaker.types.scene_summary

    out: SceneSummaries = []
    for item in data:
        out.append(capo_iottwinmaker.types.scene_summary.deserialize_json(item))
    return out
