"""Generated from Smithy shape ``com.amazonaws.cognitosync#Record``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_sync.types.date
    import capo_cognito_sync.types.long
    import capo_cognito_sync.types.record_key
    import capo_cognito_sync.types.record_value
    import capo_cognito_sync.types.string


class Record(TypedDict, closed=True):
    key: NotRequired["capo_cognito_sync.types.record_key.RecordKey"]
    """The key for the record."""
    value: NotRequired["capo_cognito_sync.types.record_value.RecordValue"]
    """The value for the record."""
    sync_count: NotRequired["capo_cognito_sync.types.long.Long"]
    """The server sync count for this record."""
    last_modified_date: NotRequired["capo_cognito_sync.types.date.Date"]
    """The date on which the record was last modified."""
    last_modified_by: NotRequired["capo_cognito_sync.types.string.String"]
    """The user/device that made the last change to this record."""
    device_last_modified_date: NotRequired["capo_cognito_sync.types.date.Date"]
    """The last modified date of the client device."""


# --- restJson1 ser/de ---
def serialize_json(value: Record) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    if "sync_count" in value:
        out["SyncCount"] = value["sync_count"]
    if "last_modified_date" in value:
        import capo_cognito_sync.types.date

        out["LastModifiedDate"] = capo_cognito_sync.types.date.serialize_json(
            value["last_modified_date"]
        )
    if "last_modified_by" in value:
        out["LastModifiedBy"] = value["last_modified_by"]
    if "device_last_modified_date" in value:
        import capo_cognito_sync.types.date

        out["DeviceLastModifiedDate"] = capo_cognito_sync.types.date.serialize_json(
            value["device_last_modified_date"]
        )
    return out


def deserialize_json(data: dict) -> Record:
    out: Record = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    if "SyncCount" in data:
        out["sync_count"] = data["SyncCount"]
    if "LastModifiedDate" in data:
        import capo_cognito_sync.types.date

        out["last_modified_date"] = capo_cognito_sync.types.date.deserialize_json(
            data["LastModifiedDate"]
        )
    if "LastModifiedBy" in data:
        out["last_modified_by"] = data["LastModifiedBy"]
    if "DeviceLastModifiedDate" in data:
        import capo_cognito_sync.types.date

        out["device_last_modified_date"] = (
            capo_cognito_sync.types.date.deserialize_json(
                data["DeviceLastModifiedDate"]
            )
        )
    return out
