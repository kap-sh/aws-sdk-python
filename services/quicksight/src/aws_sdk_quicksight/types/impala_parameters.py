"""Generated from Smithy shape ``com.amazonaws.quicksight#ImpalaParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.database
    import aws_sdk_quicksight.types.host
    import aws_sdk_quicksight.types.port
    import aws_sdk_quicksight.types.sql_endpoint_path


class ImpalaParameters(TypedDict, closed=True):
    host: "aws_sdk_quicksight.types.host.Host"
    """<p>The host name of the Impala data source.</p>"""
    port: "aws_sdk_quicksight.types.port.Port"
    """<p>The port of the Impala data source.</p>"""
    database: NotRequired["aws_sdk_quicksight.types.database.Database"]
    """<p>The database of the Impala data source.</p>"""
    sql_endpoint_path: "aws_sdk_quicksight.types.sql_endpoint_path.SqlEndpointPath"
    """<p>The HTTP path of the Impala data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImpalaParameters) -> dict:
    out: dict = {}
    out["Host"] = value["host"]
    out["Port"] = value["port"]
    if "database" in value:
        out["Database"] = value["database"]
    out["SqlEndpointPath"] = value["sql_endpoint_path"]
    return out


def deserialize_json(data: dict) -> ImpalaParameters:
    out: ImpalaParameters = {}  # type: ignore[typeddict-item]
    if "Host" in data:
        out["host"] = data["Host"]
    else:
        raise DeserializationError("ImpalaParameters.host required")
    if "Port" in data:
        out["port"] = data["Port"]
    else:
        raise DeserializationError("ImpalaParameters.port required")
    if "Database" in data:
        out["database"] = data["Database"]
    if "SqlEndpointPath" in data:
        out["sql_endpoint_path"] = data["SqlEndpointPath"]
    else:
        raise DeserializationError("ImpalaParameters.sql_endpoint_path required")
    return out
