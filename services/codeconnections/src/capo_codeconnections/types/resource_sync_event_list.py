"""Generated from Smithy shape ``com.amazonaws.codeconnections#ResourceSyncEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeconnections.types.resource_sync_event

ResourceSyncEventList: TypeAlias = list[
    "capo_codeconnections.types.resource_sync_event.ResourceSyncEvent"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceSyncEventList) -> list:
    import capo_codeconnections.types.resource_sync_event

    out: list = []
    for item in value:
        out.append(
            capo_codeconnections.types.resource_sync_event.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ResourceSyncEventList:
    import capo_codeconnections.types.resource_sync_event

    out: ResourceSyncEventList = []
    for item in data:
        out.append(
            capo_codeconnections.types.resource_sync_event.deserialize_aws_json_1_0(
                item
            )
        )
    return out
