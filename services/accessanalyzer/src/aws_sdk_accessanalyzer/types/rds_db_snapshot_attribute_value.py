"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#RdsDbSnapshotAttributeValue``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.rds_db_snapshot_account_ids_list


class _RdsDbSnapshotAttributeValue_accountIds(TypedDict):
    accountIds: "aws_sdk_accessanalyzer.types.rds_db_snapshot_account_ids_list.RdsDbSnapshotAccountIdsList"


RdsDbSnapshotAttributeValue: TypeAlias = _RdsDbSnapshotAttributeValue_accountIds


# --- restJson1 ser/de ---
def serialize_json(value: RdsDbSnapshotAttributeValue) -> dict:
    if "accountIds" in value:
        import aws_sdk_accessanalyzer.types.rds_db_snapshot_account_ids_list

        return {
            "accountIds": aws_sdk_accessanalyzer.types.rds_db_snapshot_account_ids_list.serialize_json(
                value["accountIds"]
            )
        }
    else:
        raise SerializationError("RdsDbSnapshotAttributeValue: no variant present")


def deserialize_json(data: dict) -> RdsDbSnapshotAttributeValue:
    if "accountIds" in data:
        import aws_sdk_accessanalyzer.types.rds_db_snapshot_account_ids_list

        return {
            "accountIds": aws_sdk_accessanalyzer.types.rds_db_snapshot_account_ids_list.deserialize_json(
                data["accountIds"]
            )
        }
    else:
        raise DeserializationError(
            "RdsDbSnapshotAttributeValue: no recognized variant key"
        )
