"""Generated from Smithy shape ``com.amazonaws.proton#RepositorySyncEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_proton.types.repository_sync_event

RepositorySyncEvents: TypeAlias = list[
    "aws_sdk_proton.types.repository_sync_event.RepositorySyncEvent"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RepositorySyncEvents) -> list:
    import aws_sdk_proton.types.repository_sync_event

    out: list = []
    for item in value:
        out.append(
            aws_sdk_proton.types.repository_sync_event.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RepositorySyncEvents:
    import aws_sdk_proton.types.repository_sync_event

    out: RepositorySyncEvents = []
    for item in data:
        out.append(
            aws_sdk_proton.types.repository_sync_event.deserialize_aws_json_1_0(item)
        )
    return out
