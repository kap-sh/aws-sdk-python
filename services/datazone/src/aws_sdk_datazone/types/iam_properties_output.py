"""Generated from Smithy shape ``com.amazonaws.datazone#IamPropertiesOutput``."""

from typing import TypedDict
from typing_extensions import NotRequired


class IamPropertiesOutput(TypedDict):
    environment_id: NotRequired["str"]
    """<p>The environment ID of the connection.</p>"""
    glue_lineage_sync_enabled: NotRequired["bool"]
    """<p>Specifies whether Amazon Web Services Glue lineage sync is enabled for a connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IamPropertiesOutput) -> dict:
    out: dict = {}
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "glue_lineage_sync_enabled" in value:
        out["glueLineageSyncEnabled"] = value["glue_lineage_sync_enabled"]
    return out


def deserialize_json(data: dict) -> IamPropertiesOutput:
    out: IamPropertiesOutput = {}  # type: ignore[typeddict-item]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    if "glueLineageSyncEnabled" in data:
        out["glue_lineage_sync_enabled"] = data["glueLineageSyncEnabled"]
    return out
