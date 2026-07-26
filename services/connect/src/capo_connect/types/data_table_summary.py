"""Generated from Smithy shape ``com.amazonaws.connect#DataTableSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.data_table_id
    import capo_connect.types.data_table_name
    import capo_connect.types.region_name
    import capo_connect.types.timestamp


class DataTableSummary(TypedDict, closed=True):
    name: NotRequired["capo_connect.types.data_table_name.DataTableName"]
    """<p>The summary's name.</p>"""
    id: NotRequired["capo_connect.types.data_table_id.DataTableId"]
    """<p>The summary's ID.</p>"""
    arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The summary's ARN.</p>"""
    last_modified_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The summary's last modified time.</p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p>The summary's last modified region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataTableSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "last_modified_time" in value:
        import capo_connect.types.timestamp

        out["LastModifiedTime"] = capo_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> DataTableSummary:
    out: DataTableSummary = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "LastModifiedTime" in data:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
