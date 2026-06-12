"""Generated from Smithy shape ``com.amazonaws.connect#UpdateDataTableMetadataResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_lock_version


class UpdateDataTableMetadataResponse(TypedDict):
    lock_version: "aws_sdk_connect.types.data_table_lock_version.DataTableLockVersion"
    """<p>The new lock version for the data table after the update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataTableMetadataResponse) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.data_table_lock_version

    out["LockVersion"] = aws_sdk_connect.types.data_table_lock_version.serialize_json(
        value["lock_version"]
    )
    return out


def deserialize_json(data: dict) -> UpdateDataTableMetadataResponse:
    out: UpdateDataTableMetadataResponse = {}  # type: ignore[typeddict-item]
    if "LockVersion" in data:
        import aws_sdk_connect.types.data_table_lock_version

        out["lock_version"] = (
            aws_sdk_connect.types.data_table_lock_version.deserialize_json(
                data["LockVersion"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateDataTableMetadataResponse.lock_version required"
        )
    return out
