"""Generated from Smithy shape ``com.amazonaws.drs#EbsSnapshotsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.ebs_snapshot

EbsSnapshotsList: TypeAlias = list["capo_drs.types.ebs_snapshot.EbsSnapshot"]


# --- restJson1 ser/de ---
def serialize_json(value: EbsSnapshotsList) -> list:
    return list(value)


def deserialize_json(data: list) -> EbsSnapshotsList:
    return list(data)
