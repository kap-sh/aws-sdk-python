"""Generated from Smithy shape ``com.amazonaws.appmesh#Duration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.duration_unit
    import aws_sdk_app_mesh.types.duration_value

class Duration(TypedDict):
    value: NotRequired["aws_sdk_app_mesh.types.duration_value.DurationValue"]
    """<p>A number of time units.</p>"""
    unit: NotRequired["aws_sdk_app_mesh.types.duration_unit.DurationUnit"]
    """<p>A unit of time.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: Duration) -> dict:
    out: dict = {}
    if "value" in value:
        out["value"] = value["value"]
    if "unit" in value:
        out["unit"] = value["unit"]
    return out


def deserialize_json(data: dict) -> Duration:
    out: Duration = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    if "unit" in data:
        out["unit"] = data["unit"]
    return out