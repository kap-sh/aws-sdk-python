"""Generated from Smithy shape ``com.amazonaws.cognitosync#ListRecordsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_sync.types.boolean
    import capo_cognito_sync.types.integer
    import capo_cognito_sync.types.long
    import capo_cognito_sync.types.merged_dataset_name_list
    import capo_cognito_sync.types.record_list
    import capo_cognito_sync.types.string


class ListRecordsResponse(TypedDict, closed=True):
    records: NotRequired["capo_cognito_sync.types.record_list.RecordList"]
    """A list of all records."""
    next_token: NotRequired["capo_cognito_sync.types.string.String"]
    """A pagination token for obtaining the next page of results."""
    count: "capo_cognito_sync.types.integer.Integer"
    """Total number of records."""
    dataset_sync_count: NotRequired["capo_cognito_sync.types.long.Long"]
    """Server sync count for this dataset."""
    last_modified_by: NotRequired["capo_cognito_sync.types.string.String"]
    """The user/device that made the last change to this record."""
    merged_dataset_names: NotRequired[
        "capo_cognito_sync.types.merged_dataset_name_list.MergedDatasetNameList"
    ]
    """Names of merged datasets."""
    dataset_exists: "capo_cognito_sync.types.boolean.Boolean"
    """Indicates whether the dataset exists."""
    dataset_deleted_after_requested_sync_count: (
        "capo_cognito_sync.types.boolean.Boolean"
    )
    """A boolean value specifying whether to delete the dataset locally."""
    sync_session_token: NotRequired["capo_cognito_sync.types.string.String"]
    """A token containing a session ID, identity ID, and expiration."""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecordsResponse) -> dict:
    out: dict = {}
    if "records" in value:
        import capo_cognito_sync.types.record_list

        out["Records"] = capo_cognito_sync.types.record_list.serialize_json(
            value["records"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["Count"] = value.get("count", 0)
    if "dataset_sync_count" in value:
        out["DatasetSyncCount"] = value["dataset_sync_count"]
    if "last_modified_by" in value:
        out["LastModifiedBy"] = value["last_modified_by"]
    if "merged_dataset_names" in value:
        import capo_cognito_sync.types.merged_dataset_name_list

        out["MergedDatasetNames"] = (
            capo_cognito_sync.types.merged_dataset_name_list.serialize_json(
                value["merged_dataset_names"]
            )
        )
    out["DatasetExists"] = value.get("dataset_exists", False)
    out["DatasetDeletedAfterRequestedSyncCount"] = value.get(
        "dataset_deleted_after_requested_sync_count", False
    )
    if "sync_session_token" in value:
        out["SyncSessionToken"] = value["sync_session_token"]
    return out


def deserialize_json(data: dict) -> ListRecordsResponse:
    out: ListRecordsResponse = {}  # type: ignore[typeddict-item]
    if "Records" in data:
        import capo_cognito_sync.types.record_list

        out["records"] = capo_cognito_sync.types.record_list.deserialize_json(
            data["Records"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Count" in data:
        out["count"] = data["Count"]
    else:
        out["count"] = 0
    if "DatasetSyncCount" in data:
        out["dataset_sync_count"] = data["DatasetSyncCount"]
    if "LastModifiedBy" in data:
        out["last_modified_by"] = data["LastModifiedBy"]
    if "MergedDatasetNames" in data:
        import capo_cognito_sync.types.merged_dataset_name_list

        out["merged_dataset_names"] = (
            capo_cognito_sync.types.merged_dataset_name_list.deserialize_json(
                data["MergedDatasetNames"]
            )
        )
    if "DatasetExists" in data:
        out["dataset_exists"] = data["DatasetExists"]
    else:
        out["dataset_exists"] = False
    if "DatasetDeletedAfterRequestedSyncCount" in data:
        out["dataset_deleted_after_requested_sync_count"] = data[
            "DatasetDeletedAfterRequestedSyncCount"
        ]
    else:
        out["dataset_deleted_after_requested_sync_count"] = False
    if "SyncSessionToken" in data:
        out["sync_session_token"] = data["SyncSessionToken"]
    return out
