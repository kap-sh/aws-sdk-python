"""Generated from Smithy shape ``com.amazonaws.connect#WorkspaceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.workspace_summary

WorkspaceSummaryList: TypeAlias = list[
    "capo_connect.types.workspace_summary.WorkspaceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceSummaryList) -> list:
    import capo_connect.types.workspace_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.workspace_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkspaceSummaryList:
    import capo_connect.types.workspace_summary

    out: WorkspaceSummaryList = []
    for item in data:
        out.append(capo_connect.types.workspace_summary.deserialize_json(item))
    return out
