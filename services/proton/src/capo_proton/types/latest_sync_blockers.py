"""Generated from Smithy shape ``com.amazonaws.proton#LatestSyncBlockers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_proton.types.sync_blocker

LatestSyncBlockers: TypeAlias = list["capo_proton.types.sync_blocker.SyncBlocker"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LatestSyncBlockers) -> list:
    import capo_proton.types.sync_blocker

    out: list = []
    for item in value:
        out.append(capo_proton.types.sync_blocker.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> LatestSyncBlockers:
    import capo_proton.types.sync_blocker

    out: LatestSyncBlockers = []
    for item in data:
        out.append(capo_proton.types.sync_blocker.deserialize_aws_json_1_0(item))
    return out
