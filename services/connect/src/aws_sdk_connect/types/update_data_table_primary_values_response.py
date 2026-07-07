"""Generated from Smithy shape ``com.amazonaws.connect#UpdateDataTablePrimaryValuesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_lock_version


class UpdateDataTablePrimaryValuesResponse(TypedDict, closed=True):
    lock_version: "aws_sdk_connect.types.data_table_lock_version.DataTableLockVersion"
    """<p>The updated lock version information for the data table and affected components after the primary values change.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataTablePrimaryValuesResponse) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.data_table_lock_version

    out["LockVersion"] = aws_sdk_connect.types.data_table_lock_version.serialize_json(
        value["lock_version"]
    )
    return out


def deserialize_json(data: dict) -> UpdateDataTablePrimaryValuesResponse:
    out: UpdateDataTablePrimaryValuesResponse = {}  # type: ignore[typeddict-item]
    if "LockVersion" in data:
        import aws_sdk_connect.types.data_table_lock_version

        out["lock_version"] = (
            aws_sdk_connect.types.data_table_lock_version.deserialize_json(
                data["LockVersion"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateDataTablePrimaryValuesResponse.lock_version required"
        )
    return out
