"""Generated from Smithy shape ``com.amazonaws.quicksight#PostgreSqlParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.database
    import aws_sdk_quicksight.types.host
    import aws_sdk_quicksight.types.port


class PostgreSqlParameters(TypedDict, closed=True):
    host: "aws_sdk_quicksight.types.host.Host"
    """<p>Host.</p>"""
    port: "aws_sdk_quicksight.types.port.Port"
    """<p>Port.</p>"""
    database: "aws_sdk_quicksight.types.database.Database"
    """<p>Database.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PostgreSqlParameters) -> dict:
    out: dict = {}
    out["Host"] = value["host"]
    out["Port"] = value["port"]
    out["Database"] = value["database"]
    return out


def deserialize_json(data: dict) -> PostgreSqlParameters:
    out: PostgreSqlParameters = {}  # type: ignore[typeddict-item]
    if "Host" in data:
        out["host"] = data["Host"]
    else:
        raise DeserializationError("PostgreSqlParameters.host required")
    if "Port" in data:
        out["port"] = data["Port"]
    else:
        raise DeserializationError("PostgreSqlParameters.port required")
    if "Database" in data:
        out["database"] = data["Database"]
    else:
        raise DeserializationError("PostgreSqlParameters.database required")
    return out
