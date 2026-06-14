"""Generated from Smithy shape ``com.amazonaws.datazone#IamPropertiesInput``."""

from typing import TypedDict

from typing_extensions import NotRequired


class IamPropertiesInput(TypedDict):
    glue_lineage_sync_enabled: NotRequired["bool"]
    """<p>Specifies whether Amazon Web Services Glue lineage sync is enabled for a connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IamPropertiesInput) -> dict:
    out: dict = {}
    if "glue_lineage_sync_enabled" in value:
        out["glueLineageSyncEnabled"] = value["glue_lineage_sync_enabled"]
    return out


def deserialize_json(data: dict) -> IamPropertiesInput:
    out: IamPropertiesInput = {}  # type: ignore[typeddict-item]
    if "glueLineageSyncEnabled" in data:
        out["glue_lineage_sync_enabled"] = data["glueLineageSyncEnabled"]
    return out
