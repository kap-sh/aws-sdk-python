"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#WorkspaceSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.workspace_summary

WorkspaceSummaries: TypeAlias = list[
    "capo_iottwinmaker.types.workspace_summary.WorkspaceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceSummaries) -> list:
    import capo_iottwinmaker.types.workspace_summary

    out: list = []
    for item in value:
        out.append(capo_iottwinmaker.types.workspace_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkspaceSummaries:
    import capo_iottwinmaker.types.workspace_summary

    out: WorkspaceSummaries = []
    for item in data:
        out.append(capo_iottwinmaker.types.workspace_summary.deserialize_json(item))
    return out
