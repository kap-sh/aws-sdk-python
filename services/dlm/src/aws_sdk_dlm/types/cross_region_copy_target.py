"""Generated from Smithy shape ``com.amazonaws.dlm#CrossRegionCopyTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dlm.types.target_region


class CrossRegionCopyTarget(TypedDict, closed=True):
    target_region: NotRequired["aws_sdk_dlm.types.target_region.TargetRegion"]
    """<p>The target Region, for example <code>us-east-1</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CrossRegionCopyTarget) -> dict:
    out: dict = {}
    if "target_region" in value:
        out["TargetRegion"] = value["target_region"]
    return out


def deserialize_json(data: dict) -> CrossRegionCopyTarget:
    out: CrossRegionCopyTarget = {}  # type: ignore[typeddict-item]
    if "TargetRegion" in data:
        out["target_region"] = data["TargetRegion"]
    return out
