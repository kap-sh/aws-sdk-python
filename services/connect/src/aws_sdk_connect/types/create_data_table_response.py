"""Generated from Smithy shape ``com.amazonaws.connect#CreateDataTableResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.data_table_id
    import aws_sdk_connect.types.data_table_lock_version


class CreateDataTableResponse(TypedDict):
    id: "aws_sdk_connect.types.data_table_id.DataTableId"
    """<p>The unique identifier for the created data table. Does not include the version alias.</p>"""
    arn: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) for the created data table. Does not include the version alias.</p>"""
    lock_version: "aws_sdk_connect.types.data_table_lock_version.DataTableLockVersion"
    """<p>The lock version information for the created data table, used for optimistic locking and table versioning.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataTableResponse) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["Arn"] = value["arn"]
    import aws_sdk_connect.types.data_table_lock_version

    out["LockVersion"] = aws_sdk_connect.types.data_table_lock_version.serialize_json(
        value["lock_version"]
    )
    return out


def deserialize_json(data: dict) -> CreateDataTableResponse:
    out: CreateDataTableResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("CreateDataTableResponse.id required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("CreateDataTableResponse.arn required")
    if "LockVersion" in data:
        import aws_sdk_connect.types.data_table_lock_version

        out["lock_version"] = (
            aws_sdk_connect.types.data_table_lock_version.deserialize_json(
                data["LockVersion"]
            )
        )
    else:
        raise DeserializationError("CreateDataTableResponse.lock_version required")
    return out
