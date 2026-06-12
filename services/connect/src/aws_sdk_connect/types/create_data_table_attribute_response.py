"""Generated from Smithy shape ``com.amazonaws.connect#CreateDataTableAttributeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_id
    import aws_sdk_connect.types.data_table_lock_version
    import aws_sdk_connect.types.data_table_name


class CreateDataTableAttributeResponse(TypedDict):
    name: "aws_sdk_connect.types.data_table_name.DataTableName"
    """<p>The name of the created attribute since it also serves as the identifier. This could be different than the parameter passed in since it will be trimmed for whitespace.</p>"""
    attribute_id: NotRequired["aws_sdk_connect.types.data_table_id.DataTableId"]
    """<p>The unique identifier assigned to the created attribute.</p>"""
    lock_version: "aws_sdk_connect.types.data_table_lock_version.DataTableLockVersion"
    """<p>The lock version information for the data table and attribute, used for optimistic locking and versioning.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataTableAttributeResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "attribute_id" in value:
        out["AttributeId"] = value["attribute_id"]
    import aws_sdk_connect.types.data_table_lock_version

    out["LockVersion"] = aws_sdk_connect.types.data_table_lock_version.serialize_json(
        value["lock_version"]
    )
    return out


def deserialize_json(data: dict) -> CreateDataTableAttributeResponse:
    out: CreateDataTableAttributeResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateDataTableAttributeResponse.name required")
    if "AttributeId" in data:
        out["attribute_id"] = data["AttributeId"]
    if "LockVersion" in data:
        import aws_sdk_connect.types.data_table_lock_version

        out["lock_version"] = (
            aws_sdk_connect.types.data_table_lock_version.deserialize_json(
                data["LockVersion"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDataTableAttributeResponse.lock_version required"
        )
    return out
