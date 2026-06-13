"""Generated from Smithy shape ``com.amazonaws.datazone#LakehousePropertiesOutput``."""

from typing import TypedDict
from typing_extensions import NotRequired


class LakehousePropertiesOutput(TypedDict):
    glue_lineage_sync_enabled: NotRequired["bool"]
    """<p>Specifies whether Glue lineage sync is enabled for tables managed by Glue crawlers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LakehousePropertiesOutput) -> dict:
    out: dict = {}
    if "glue_lineage_sync_enabled" in value:
        out["glueLineageSyncEnabled"] = value["glue_lineage_sync_enabled"]
    return out


def deserialize_json(data: dict) -> LakehousePropertiesOutput:
    out: LakehousePropertiesOutput = {}  # type: ignore[typeddict-item]
    if "glueLineageSyncEnabled" in data:
        out["glue_lineage_sync_enabled"] = data["glueLineageSyncEnabled"]
    return out
