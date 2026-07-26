"""Generated from Smithy shape ``com.amazonaws.connect#DataTableLockVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.string


class DataTableLockVersion(TypedDict, closed=True):
    data_table: NotRequired["capo_connect.types.string.String"]
    """<p>The lock version for the data table itself. Used for optimistic locking and table versioning. Changes with each update to the table's metadata or structure.</p>"""
    attribute: NotRequired["capo_connect.types.string.String"]
    """<p>The lock version for a specific attribute. When the ValueLockLevel is ATTRIBUTE, this version changes when any value for the attribute changes. For other lock levels, it only changes when the attribute's properties are directly updated.</p>"""
    primary_values: NotRequired["capo_connect.types.string.String"]
    """<p>The lock version for a specific set of primary values (record). This includes the default record even if the table does not have any primary attributes. Used for record-level locking.</p>"""
    value: NotRequired["capo_connect.types.string.String"]
    """<p>The lock version for a specific value. Changes each time the individual value is modified. Used for the finest-grained locking control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataTableLockVersion) -> dict:
    out: dict = {}
    if "data_table" in value:
        out["DataTable"] = value["data_table"]
    if "attribute" in value:
        out["Attribute"] = value["attribute"]
    if "primary_values" in value:
        out["PrimaryValues"] = value["primary_values"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> DataTableLockVersion:
    out: DataTableLockVersion = {}  # type: ignore[typeddict-item]
    if "DataTable" in data:
        out["data_table"] = data["DataTable"]
    if "Attribute" in data:
        out["attribute"] = data["Attribute"]
    if "PrimaryValues" in data:
        out["primary_values"] = data["PrimaryValues"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
