"""Generated from Smithy shape ``com.amazonaws.cognitosync#Dataset``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_sync.types.dataset_name
    import capo_cognito_sync.types.date
    import capo_cognito_sync.types.identity_id
    import capo_cognito_sync.types.long
    import capo_cognito_sync.types.string


class Dataset(TypedDict, closed=True):
    identity_id: NotRequired["capo_cognito_sync.types.identity_id.IdentityId"]
    """A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region."""
    dataset_name: NotRequired["capo_cognito_sync.types.dataset_name.DatasetName"]
    """A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '_' (underscore), '-' (dash), and '.' (dot)."""
    creation_date: NotRequired["capo_cognito_sync.types.date.Date"]
    """Date on which the dataset was created."""
    last_modified_date: NotRequired["capo_cognito_sync.types.date.Date"]
    """Date when the dataset was last modified."""
    last_modified_by: NotRequired["capo_cognito_sync.types.string.String"]
    """The device that made the last change to this dataset."""
    data_storage: NotRequired["capo_cognito_sync.types.long.Long"]
    """Total size in bytes of the records in this dataset."""
    num_records: NotRequired["capo_cognito_sync.types.long.Long"]
    """Number of records in this dataset."""


# --- restJson1 ser/de ---
def serialize_json(value: Dataset) -> dict:
    out: dict = {}
    if "identity_id" in value:
        out["IdentityId"] = value["identity_id"]
    if "dataset_name" in value:
        out["DatasetName"] = value["dataset_name"]
    if "creation_date" in value:
        import capo_cognito_sync.types.date

        out["CreationDate"] = capo_cognito_sync.types.date.serialize_json(
            value["creation_date"]
        )
    if "last_modified_date" in value:
        import capo_cognito_sync.types.date

        out["LastModifiedDate"] = capo_cognito_sync.types.date.serialize_json(
            value["last_modified_date"]
        )
    if "last_modified_by" in value:
        out["LastModifiedBy"] = value["last_modified_by"]
    if "data_storage" in value:
        out["DataStorage"] = value["data_storage"]
    if "num_records" in value:
        out["NumRecords"] = value["num_records"]
    return out


def deserialize_json(data: dict) -> Dataset:
    out: Dataset = {}  # type: ignore[typeddict-item]
    if "IdentityId" in data:
        out["identity_id"] = data["IdentityId"]
    if "DatasetName" in data:
        out["dataset_name"] = data["DatasetName"]
    if "CreationDate" in data:
        import capo_cognito_sync.types.date

        out["creation_date"] = capo_cognito_sync.types.date.deserialize_json(
            data["CreationDate"]
        )
    if "LastModifiedDate" in data:
        import capo_cognito_sync.types.date

        out["last_modified_date"] = capo_cognito_sync.types.date.deserialize_json(
            data["LastModifiedDate"]
        )
    if "LastModifiedBy" in data:
        out["last_modified_by"] = data["LastModifiedBy"]
    if "DataStorage" in data:
        out["data_storage"] = data["DataStorage"]
    if "NumRecords" in data:
        out["num_records"] = data["NumRecords"]
    return out
