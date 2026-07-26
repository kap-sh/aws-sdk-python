"""Generated from Smithy shape ``com.amazonaws.mgn#TerminateTargetInstancesRequestSourceServerIDs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.source_server_id

TerminateTargetInstancesRequestSourceServerIDs: TypeAlias = list[
    "capo_mgn.types.source_server_id.SourceServerID"
]


# --- restJson1 ser/de ---
def serialize_json(value: TerminateTargetInstancesRequestSourceServerIDs) -> list:
    return list(value)


def deserialize_json(data: list) -> TerminateTargetInstancesRequestSourceServerIDs:
    return list(data)
