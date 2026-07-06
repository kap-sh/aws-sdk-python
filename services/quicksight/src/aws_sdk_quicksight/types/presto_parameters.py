"""Generated from Smithy shape ``com.amazonaws.quicksight#PrestoParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.catalog
    import aws_sdk_quicksight.types.host
    import aws_sdk_quicksight.types.port


class PrestoParameters(TypedDict, closed=True):
    host: "aws_sdk_quicksight.types.host.Host"
    """<p>Host.</p>"""
    port: "aws_sdk_quicksight.types.port.Port"
    """<p>Port.</p>"""
    catalog: "aws_sdk_quicksight.types.catalog.Catalog"
    """<p>Catalog.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrestoParameters) -> dict:
    out: dict = {}
    out["Host"] = value["host"]
    out["Port"] = value["port"]
    out["Catalog"] = value["catalog"]
    return out


def deserialize_json(data: dict) -> PrestoParameters:
    out: PrestoParameters = {}  # type: ignore[typeddict-item]
    if "Host" in data:
        out["host"] = data["Host"]
    else:
        raise DeserializationError("PrestoParameters.host required")
    if "Port" in data:
        out["port"] = data["Port"]
    else:
        raise DeserializationError("PrestoParameters.port required")
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("PrestoParameters.catalog required")
    return out
