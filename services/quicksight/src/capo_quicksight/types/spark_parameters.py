"""Generated from Smithy shape ``com.amazonaws.quicksight#SparkParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.host
    import capo_quicksight.types.port


class SparkParameters(TypedDict, closed=True):
    host: "capo_quicksight.types.host.Host"
    """<p>Host.</p>"""
    port: "capo_quicksight.types.port.Port"
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
