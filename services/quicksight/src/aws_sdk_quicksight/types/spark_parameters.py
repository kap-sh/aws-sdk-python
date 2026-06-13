"""Generated from Smithy shape ``com.amazonaws.quicksight#SparkParameters``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.host
    import aws_sdk_quicksight.types.port


class SparkParameters(TypedDict):
    host: "aws_sdk_quicksight.types.host.Host"
    """<p>Host.</p>"""
    port: "aws_sdk_quicksight.types.port.Port"
    """<p>Port.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SparkParameters) -> dict:
    out: dict = {}
    out["Host"] = value["host"]
    out["Port"] = value["port"]
    return out


def deserialize_json(data: dict) -> SparkParameters:
    out: SparkParameters = {}  # type: ignore[typeddict-item]
    if "Host" in data:
        out["host"] = data["Host"]
    else:
        raise DeserializationError("SparkParameters.host required")
    if "Port" in data:
        out["port"] = data["Port"]
    else:
        raise DeserializationError("SparkParameters.port required")
    return out
