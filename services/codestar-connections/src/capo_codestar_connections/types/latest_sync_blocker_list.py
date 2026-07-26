"""Generated from Smithy shape ``com.amazonaws.codestarconnections#LatestSyncBlockerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codestar_connections.types.sync_blocker

LatestSyncBlockerList: TypeAlias = list[
    "capo_codestar_connections.types.sync_blocker.SyncBlocker"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LatestSyncBlockerList) -> list:
    import capo_codestar_connections.types.sync_blocker

    out: list = []
    for item in value:
        out.append(
            capo_codestar_connections.types.sync_blocker.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> LatestSyncBlockerList:
    import capo_codestar_connections.types.sync_blocker

    out: LatestSyncBlockerList = []
    for item in data:
        out.append(
            capo_codestar_connections.types.sync_blocker.deserialize_aws_json_1_0(item)
        )
    return out
