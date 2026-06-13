"""Generated from Smithy shape ``com.amazonaws.odb#DbIormConfig``."""

from typing import TypedDict

from typing_extensions import NotRequired


class DbIormConfig(TypedDict):
    db_name: NotRequired["str"]
    """<p>The database name. For the default DbPlan, the dbName is <code>default</code>.</p>"""
    flash_cache_limit: NotRequired["str"]
    """<p>The flash cache limit for this database. This value is internally configured based on the share value assigned to the database.</p>"""
    share: NotRequired["int"]
    """<p>The relative priority of this database.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbIormConfig) -> dict:
    out: dict = {}
    if "db_name" in value:
        out["dbName"] = value["db_name"]
    if "flash_cache_limit" in value:
        out["flashCacheLimit"] = value["flash_cache_limit"]
    if "share" in value:
        out["share"] = value["share"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DbIormConfig:
    out: DbIormConfig = {}  # type: ignore[typeddict-item]
    if "dbName" in data:
        out["db_name"] = data["dbName"]
    if "flashCacheLimit" in data:
        out["flash_cache_limit"] = data["flashCacheLimit"]
    if "share" in data:
        out["share"] = data["share"]
    return out
