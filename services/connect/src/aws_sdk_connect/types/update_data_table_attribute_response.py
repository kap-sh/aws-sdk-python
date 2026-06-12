"""Generated from Smithy shape ``com.amazonaws.connect#UpdateDataTableAttributeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_lock_version
    import aws_sdk_connect.types.data_table_name


class UpdateDataTableAttributeResponse(TypedDict):
    name: "aws_sdk_connect.types.data_table_name.DataTableName"
    """<p>The trimmed name and identifier for the updated attribute.</p>"""
    lock_version: "aws_sdk_connect.types.data_table_lock_version.DataTableLockVersion"
    """<p>The new lock version for the attribute after the update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataTableAttributeResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_connect.types.data_table_lock_version

    out["LockVersion"] = aws_sdk_connect.types.data_table_lock_version.serialize_json(
        value["lock_version"]
    )
    return out


def deserialize_json(data: dict) -> UpdateDataTableAttributeResponse:
    out: UpdateDataTableAttributeResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateDataTableAttributeResponse.name required")
    if "LockVersion" in data:
        import aws_sdk_connect.types.data_table_lock_version

        out["lock_version"] = (
            aws_sdk_connect.types.data_table_lock_version.deserialize_json(
                data["LockVersion"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateDataTableAttributeResponse.lock_version required"
        )
    return out
