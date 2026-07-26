"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#SyncResourceSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.sync_resource_summary

SyncResourceSummaries: TypeAlias = list[
    "capo_iottwinmaker.types.sync_resource_summary.SyncResourceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SyncResourceSummaries) -> list:
    import capo_iottwinmaker.types.sync_resource_summary

    out: list = []
    for item in value:
        out.append(capo_iottwinmaker.types.sync_resource_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> SyncResourceSummaries:
    import capo_iottwinmaker.types.sync_resource_summary

    out: SyncResourceSummaries = []
    for item in data:
        out.append(capo_iottwinmaker.types.sync_resource_summary.deserialize_json(item))
    return out
