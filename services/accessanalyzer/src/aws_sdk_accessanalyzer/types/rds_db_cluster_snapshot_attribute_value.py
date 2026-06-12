"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#RdsDbClusterSnapshotAttributeValue``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.rds_db_cluster_snapshot_account_ids_list


class _RdsDbClusterSnapshotAttributeValue_accountIds(TypedDict):
    accountIds: "aws_sdk_accessanalyzer.types.rds_db_cluster_snapshot_account_ids_list.RdsDbClusterSnapshotAccountIdsList"


RdsDbClusterSnapshotAttributeValue: TypeAlias = (
    _RdsDbClusterSnapshotAttributeValue_accountIds
)


# --- restJson1 ser/de ---
def serialize_json(value: RdsDbClusterSnapshotAttributeValue) -> dict:
    if "accountIds" in value:
        import aws_sdk_accessanalyzer.types.rds_db_cluster_snapshot_account_ids_list

        return {
            "accountIds": aws_sdk_accessanalyzer.types.rds_db_cluster_snapshot_account_ids_list.serialize_json(
                value["accountIds"]
            )
        }
    else:
        raise SerializationError(
            "RdsDbClusterSnapshotAttributeValue: no variant present"
        )


def deserialize_json(data: dict) -> RdsDbClusterSnapshotAttributeValue:
    if "accountIds" in data:
        import aws_sdk_accessanalyzer.types.rds_db_cluster_snapshot_account_ids_list

        return {
            "accountIds": aws_sdk_accessanalyzer.types.rds_db_cluster_snapshot_account_ids_list.deserialize_json(
                data["accountIds"]
            )
        }
    else:
        raise DeserializationError(
            "RdsDbClusterSnapshotAttributeValue: no recognized variant key"
        )
