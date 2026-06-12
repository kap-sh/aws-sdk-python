"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#RdsDbSnapshotAccountIdsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.rds_db_snapshot_account_id

RdsDbSnapshotAccountIdsList: TypeAlias = list[
    "aws_sdk_accessanalyzer.types.rds_db_snapshot_account_id.RdsDbSnapshotAccountId"
]


# --- restJson1 ser/de ---
def serialize_json(value: RdsDbSnapshotAccountIdsList) -> list:
    return list(value)


def deserialize_json(data: list) -> RdsDbSnapshotAccountIdsList:
    return list(data)
