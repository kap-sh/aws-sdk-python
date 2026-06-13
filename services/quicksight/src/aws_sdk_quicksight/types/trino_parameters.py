"""Generated from Smithy shape ``com.amazonaws.quicksight#TrinoParameters``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.catalog
    import aws_sdk_quicksight.types.host
    import aws_sdk_quicksight.types.port


class TrinoParameters(TypedDict):
    host: "aws_sdk_quicksight.types.host.Host"
    """<p>The host name of the Trino data source.</p>"""
    port: "aws_sdk_quicksight.types.port.Port"
    """<p>The port for the Trino data source.</p>"""
    catalog: "aws_sdk_quicksight.types.catalog.Catalog"
    """<p>The catalog name for the Trino data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrinoParameters) -> dict:
    out: dict = {}
    out["Host"] = value["host"]
    out["Port"] = value["port"]
    out["Catalog"] = value["catalog"]
    return out


def deserialize_json(data: dict) -> TrinoParameters:
    out: TrinoParameters = {}  # type: ignore[typeddict-item]
    if "Host" in data:
        out["host"] = data["Host"]
    else:
        raise DeserializationError("TrinoParameters.host required")
    if "Port" in data:
        out["port"] = data["Port"]
    else:
        raise DeserializationError("TrinoParameters.port required")
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("TrinoParameters.catalog required")
    return out
