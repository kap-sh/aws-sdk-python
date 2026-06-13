"""Generated from Smithy shape ``com.amazonaws.proton#ResourceSyncEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_proton.types.resource_sync_event

ResourceSyncEvents: TypeAlias = list[
    "aws_sdk_proton.types.resource_sync_event.ResourceSyncEvent"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceSyncEvents) -> list:
    import aws_sdk_proton.types.resource_sync_event

    out: list = []
    for item in value:
        out.append(
            aws_sdk_proton.types.resource_sync_event.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ResourceSyncEvents:
    import aws_sdk_proton.types.resource_sync_event

    out: ResourceSyncEvents = []
    for item in data:
        out.append(
            aws_sdk_proton.types.resource_sync_event.deserialize_aws_json_1_0(item)
        )
    return out
