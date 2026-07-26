"""Generated from Smithy shape ``com.amazonaws.quicksight#AuroraPostgreSqlParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.database
    import capo_quicksight.types.host
    import capo_quicksight.types.port


class AuroraPostgreSqlParameters(TypedDict, closed=True):
    host: "capo_quicksight.types.host.Host"
    """<p>The Amazon Aurora PostgreSQL-Compatible host to connect to.</p>"""
    port: "capo_quicksight.types.port.Port"
    """<p>The port that Amazon Aurora PostgreSQL is listening on.</p>"""
    database: "capo_quicksight.types.database.Database"
    """<p>The Amazon Aurora PostgreSQL database to connect to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuroraPostgreSqlParameters) -> dict:
    out: dict = {}
    out["Host"] = value["host"]
    out["Port"] = value["port"]
    out["Database"] = value["database"]
    return out


def deserialize_json(data: dict) -> AuroraPostgreSqlParameters:
    out: AuroraPostgreSqlParameters = {}  # type: ignore[typeddict-item]
    if "Host" in data:
        out["host"] = data["Host"]
    else:
        raise DeserializationError("AuroraPostgreSqlParameters.host required")
    if "Port" in data:
        out["port"] = data["Port"]
    else:
        raise DeserializationError("AuroraPostgreSqlParameters.port required")
    if "Database" in data:
        out["database"] = data["Database"]
    else:
        raise DeserializationError("AuroraPostgreSqlParameters.database required")
    return out
