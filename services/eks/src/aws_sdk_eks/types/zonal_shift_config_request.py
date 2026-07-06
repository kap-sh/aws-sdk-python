"""Generated from Smithy shape ``com.amazonaws.eks#ZonalShiftConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.boxed_boolean


class ZonalShiftConfigRequest(TypedDict, closed=True):
    enabled: NotRequired["aws_sdk_eks.types.boxed_boolean.BoxedBoolean"]
    """<p>If zonal shift is enabled, Amazon Web Services configures zonal autoshift for the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ZonalShiftConfigRequest) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> ZonalShiftConfigRequest:
    out: ZonalShiftConfigRequest = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    return out
