"""Generated from Smithy shape ``com.amazonaws.connect#DeleteDataTableAttributeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.data_table_lock_version


class DeleteDataTableAttributeResponse(TypedDict, closed=True):
    lock_version: "capo_connect.types.data_table_lock_version.DataTableLockVersion"
    """<p>The updated lock version of the data table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataTableAttributeResponse) -> dict:
    out: dict = {}
    import capo_connect.types.data_table_lock_version

    out["LockVersion"] = capo_connect.types.data_table_lock_version.serialize_json(
        value["lock_version"]
    )
    return out


def deserialize_json(data: dict) -> DeleteDataTableAttributeResponse:
    out: DeleteDataTableAttributeResponse = {}  # type: ignore[typeddict-item]
    if "LockVersion" in data:
        import capo_connect.types.data_table_lock_version

        out["lock_version"] = (
            capo_connect.types.data_table_lock_version.deserialize_json(
                data["LockVersion"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteDataTableAttributeResponse.lock_version required"
        )
    return out
