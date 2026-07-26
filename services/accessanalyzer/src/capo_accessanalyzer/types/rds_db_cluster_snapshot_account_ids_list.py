"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#RdsDbClusterSnapshotAccountIdsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_accessanalyzer.types.rds_db_cluster_snapshot_account_id

RdsDbClusterSnapshotAccountIdsList: TypeAlias = list[
    "capo_accessanalyzer.types.rds_db_cluster_snapshot_account_id.RdsDbClusterSnapshotAccountId"
]


# --- restJson1 ser/de ---
def serialize_json(value: RdsDbClusterSnapshotAccountIdsList) -> list:
    return list(value)


def deserialize_json(data: list) -> RdsDbClusterSnapshotAccountIdsList:
    return list(data)
