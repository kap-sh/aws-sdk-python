"""Generated from Smithy shape ``com.amazonaws.quicksight#DatabricksParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.host
    import capo_quicksight.types.port
    import capo_quicksight.types.sql_endpoint_path


class DatabricksParameters(TypedDict, closed=True):
    host: "capo_quicksight.types.host.Host"
    """<p>The host name of the Databricks data source.</p>"""
    port: "capo_quicksight.types.port.Port"
    """<p>The port for the Databricks data source.</p>"""
    sql_endpoint_path: "capo_quicksight.types.sql_endpoint_path.SqlEndpointPath"
    """<p>The HTTP path of the Databricks data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatabricksParameters) -> dict:
    out: dict = {}
    out["Host"] = value["host"]
    out["Port"] = value["port"]
    out["SqlEndpointPath"] = value["sql_endpoint_path"]
    return out


def deserialize_json(data: dict) -> DatabricksParameters:
    out: DatabricksParameters = {}  # type: ignore[typeddict-item]
    if "Host" in data:
        out["host"] = data["Host"]
    else:
        raise DeserializationError("DatabricksParameters.host required")
    if "Port" in data:
        out["port"] = data["Port"]
    else:
        raise DeserializationError("DatabricksParameters.port required")
    if "SqlEndpointPath" in data:
        out["sql_endpoint_path"] = data["SqlEndpointPath"]
    else:
        raise DeserializationError("DatabricksParameters.sql_endpoint_path required")
    return out
