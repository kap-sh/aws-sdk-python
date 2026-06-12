"""Generated from Smithy shape ``com.amazonaws.appsync#DeltaSyncConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.long
    import aws_sdk_appsync.types.string


class DeltaSyncConfig(TypedDict):
    base_table_ttl: "aws_sdk_appsync.types.long.Long"
    """<p>The number of minutes that an Item is stored in the data source.</p>"""
    delta_sync_table_name: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>The Delta Sync table name.</p>"""
    delta_sync_table_ttl: "aws_sdk_appsync.types.long.Long"
    """<p>The number of minutes that a Delta Sync log entry is stored in the Delta Sync table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeltaSyncConfig) -> dict:
    out: dict = {}
    out["baseTableTTL"] = value.get("base_table_ttl", 0)
    if "delta_sync_table_name" in value:
        out["deltaSyncTableName"] = value["delta_sync_table_name"]
    out["deltaSyncTableTTL"] = value.get("delta_sync_table_ttl", 0)
    return out


def deserialize_json(data: dict) -> DeltaSyncConfig:
    out: DeltaSyncConfig = {}  # type: ignore[typeddict-item]
    if "baseTableTTL" in data:
        out["base_table_ttl"] = data["baseTableTTL"]
    else:
        out["base_table_ttl"] = 0
    if "deltaSyncTableName" in data:
        out["delta_sync_table_name"] = data["deltaSyncTableName"]
    if "deltaSyncTableTTL" in data:
        out["delta_sync_table_ttl"] = data["deltaSyncTableTTL"]
    else:
        out["delta_sync_table_ttl"] = 0
    return out
