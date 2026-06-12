"""Generated from Smithy shape ``com.amazonaws.mgn#CPU``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_mgn.types.bounded_string
    import aws_sdk_mgn.types.positive_integer

class CPU(TypedDict):
    cores: "aws_sdk_mgn.types.positive_integer.PositiveInteger"
    """<p>The number of CPU cores on the source server.</p>"""
    model_name: NotRequired["aws_sdk_mgn.types.bounded_string.BoundedString"]
    """<p>The source server's CPU model name.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CPU) -> dict:
    out: dict = {}
    out["cores"] = value.get("cores", 0)
    if "model_name" in value:
        out["modelName"] = value["model_name"]
    return out


def deserialize_json(data: dict) -> CPU:
    out: CPU = {}  # type: ignore[typeddict-item]
    if "cores" in data:
        out["cores"] = data["cores"]
    else:
        out["cores"] = 0
    if "modelName" in data:
        out["model_name"] = data["modelName"]
    return out