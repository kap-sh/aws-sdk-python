"""Generated from Smithy shape ``com.amazonaws.quicksight#OracleParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.boolean
    import capo_quicksight.types.database
    import capo_quicksight.types.host
    import capo_quicksight.types.port


class OracleParameters(TypedDict, closed=True):
    host: "capo_quicksight.types.host.Host"
    """<p>An Oracle host.</p>"""
    port: "capo_quicksight.types.port.Port"
    """<p>The port.</p>"""
    database: "capo_quicksight.types.database.Database"
    """<p>The database.</p>"""
    use_service_name: "capo_quicksight.types.boolean.Boolean"
    """<p>A Boolean value that indicates whether the <code>Database</code> uses a service name or an SID. If this value is left blank, the default value is <code>SID</code>. If this value is set to <code>false</code>, the value is <code>SID</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OracleParameters) -> dict:
    out: dict = {}
    out["Host"] = value["host"]
    out["Port"] = value["port"]
    out["Database"] = value["database"]
    out["UseServiceName"] = value.get("use_service_name", False)
    return out


def deserialize_json(data: dict) -> OracleParameters:
    out: OracleParameters = {}  # type: ignore[typeddict-item]
    if "Host" in data:
        out["host"] = data["Host"]
    else:
        raise DeserializationError("OracleParameters.host required")
    if "Port" in data:
        out["port"] = data["Port"]
    else:
        raise DeserializationError("OracleParameters.port required")
    if "Database" in data:
        out["database"] = data["Database"]
    else:
        raise DeserializationError("OracleParameters.database required")
    if "UseServiceName" in data:
        out["use_service_name"] = data["UseServiceName"]
    else:
        out["use_service_name"] = False
    return out
