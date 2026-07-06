"""Generated from Smithy shape ``com.amazonaws.datazone#IamPropertiesPatch``."""

from typing_extensions import NotRequired, TypedDict


class IamPropertiesPatch(TypedDict, closed=True):
    glue_lineage_sync_enabled: NotRequired["bool"]
    """<p>Specifies whether Amazon Web Services Glue lineage sync is enabled for a connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IamPropertiesPatch) -> dict:
    out: dict = {}
    if "glue_lineage_sync_enabled" in value:
        out["glueLineageSyncEnabled"] = value["glue_lineage_sync_enabled"]
    return out


def deserialize_json(data: dict) -> IamPropertiesPatch:
    out: IamPropertiesPatch = {}  # type: ignore[typeddict-item]
    if "glueLineageSyncEnabled" in data:
        out["glue_lineage_sync_enabled"] = data["glueLineageSyncEnabled"]
    return out
