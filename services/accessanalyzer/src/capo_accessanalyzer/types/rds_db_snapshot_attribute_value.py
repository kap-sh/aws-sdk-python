"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#RdsDbSnapshotAttributeValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_accessanalyzer.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_accessanalyzer.types.rds_db_snapshot_account_ids_list


class _RdsDbSnapshotAttributeValue_accountIds(TypedDict, closed=True):
    accountIds: "capo_accessanalyzer.types.rds_db_snapshot_account_ids_list.RdsDbSnapshotAccountIdsList"


RdsDbSnapshotAttributeValue: TypeAlias = _RdsDbSnapshotAttributeValue_accountIds


# --- restJson1 ser/de ---
def serialize_json(value: RdsDbSnapshotAttributeValue) -> dict:
    if "accountIds" in value:
        import capo_accessanalyzer.types.rds_db_snapshot_account_ids_list

        return {
            "accountIds": capo_accessanalyzer.types.rds_db_snapshot_account_ids_list.serialize_json(
                value["accountIds"]
            )
        }
    else:
        raise SerializationError("RdsDbSnapshotAttributeValue: no variant present")


def deserialize_json(data: dict) -> RdsDbSnapshotAttributeValue:
    if "accountIds" in data:
        import capo_accessanalyzer.types.rds_db_snapshot_account_ids_list

        return {
            "accountIds": capo_accessanalyzer.types.rds_db_snapshot_account_ids_list.deserialize_json(
                data["accountIds"]
            )
        }
    else:
        raise DeserializationError(
            "RdsDbSnapshotAttributeValue: no recognized variant key"
        )
