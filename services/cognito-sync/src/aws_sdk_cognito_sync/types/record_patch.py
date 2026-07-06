"""Generated from Smithy shape ``com.amazonaws.cognitosync#RecordPatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cognito_sync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_sync.types.date
    import aws_sdk_cognito_sync.types.long
    import aws_sdk_cognito_sync.types.operation
    import aws_sdk_cognito_sync.types.record_key
    import aws_sdk_cognito_sync.types.record_value


class RecordPatch(TypedDict, closed=True):
    op: "aws_sdk_cognito_sync.types.operation.Operation"
    """An operation, either replace or remove."""
    key: "aws_sdk_cognito_sync.types.record_key.RecordKey"
    """The key associated with the record patch."""
    value: NotRequired["aws_sdk_cognito_sync.types.record_value.RecordValue"]
    """The value associated with the record patch."""
    sync_count: "aws_sdk_cognito_sync.types.long.Long"
    """Last known server sync count for this record. Set to 0 if unknown."""
    device_last_modified_date: NotRequired["aws_sdk_cognito_sync.types.date.Date"]
    """The last modified date of the client device."""


# --- restJson1 ser/de ---
def serialize_json(value: RecordPatch) -> dict:
    out: dict = {}
    import aws_sdk_cognito_sync.types.operation

    out["Op"] = aws_sdk_cognito_sync.types.operation.serialize_json(value["op"])
    out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    out["SyncCount"] = value["sync_count"]
    if "device_last_modified_date" in value:
        import aws_sdk_cognito_sync.types.date

        out["DeviceLastModifiedDate"] = aws_sdk_cognito_sync.types.date.serialize_json(
            value["device_last_modified_date"]
        )
    return out


def deserialize_json(data: dict) -> RecordPatch:
    out: RecordPatch = {}  # type: ignore[typeddict-item]
    if "Op" in data:
        import aws_sdk_cognito_sync.types.operation

        out["op"] = aws_sdk_cognito_sync.types.operation.deserialize_json(data["Op"])
    else:
        raise DeserializationError("RecordPatch.op required")
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("RecordPatch.key required")
    if "Value" in data:
        out["value"] = data["Value"]
    if "SyncCount" in data:
        out["sync_count"] = data["SyncCount"]
    else:
        raise DeserializationError("RecordPatch.sync_count required")
    if "DeviceLastModifiedDate" in data:
        import aws_sdk_cognito_sync.types.date

        out["device_last_modified_date"] = (
            aws_sdk_cognito_sync.types.date.deserialize_json(
                data["DeviceLastModifiedDate"]
            )
        )
    return out
