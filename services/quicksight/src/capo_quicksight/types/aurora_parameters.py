"""Generated from Smithy shape ``com.amazonaws.quicksight#AuroraParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.database
    import capo_quicksight.types.host
    import capo_quicksight.types.port


class AuroraParameters(TypedDict, closed=True):
    host: "capo_quicksight.types.host.Host"
    """<p>Host.</p>"""
    port: "capo_quicksight.types.port.Port"
    """<p>Port.</p>"""
    database: "capo_quicksight.types.database.Database"
    """<p>Database.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuroraParameters) -> dict:
    out: dict = {}
    out["Host"] = value["host"]
    out["Port"] = value["port"]
    out["Database"] = value["database"]
    return out


def deserialize_json(data: dict) -> AuroraParameters:
    out: AuroraParameters = {}  # type: ignore[typeddict-item]
    if "Host" in data:
        out["host"] = data["Host"]
    else:
        raise DeserializationError("AuroraParameters.host required")
    if "Port" in data:
        out["port"] = data["Port"]
    else:
        raise DeserializationError("AuroraParameters.port required")
    if "Database" in data:
        out["database"] = data["Database"]
    else:
        raise DeserializationError("AuroraParameters.database required")
    return out
