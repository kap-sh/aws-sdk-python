"""Generated from Smithy shape ``com.amazonaws.codestarconnections#RepositorySyncEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codestar_connections.types.repository_sync_event

RepositorySyncEventList: TypeAlias = list[
    "capo_codestar_connections.types.repository_sync_event.RepositorySyncEvent"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RepositorySyncEventList) -> list:
    import capo_codestar_connections.types.repository_sync_event

    out: list = []
    for item in value:
        out.append(
            capo_codestar_connections.types.repository_sync_event.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RepositorySyncEventList:
    import capo_codestar_connections.types.repository_sync_event

    out: RepositorySyncEventList = []
    for item in data:
        out.append(
            capo_codestar_connections.types.repository_sync_event.deserialize_aws_json_1_0(
                item
            )
        )
    return out
