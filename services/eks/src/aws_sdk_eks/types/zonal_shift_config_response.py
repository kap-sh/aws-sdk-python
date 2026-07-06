"""Generated from Smithy shape ``com.amazonaws.eks#ZonalShiftConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.boxed_boolean


class ZonalShiftConfigResponse(TypedDict, closed=True):
    enabled: NotRequired["aws_sdk_eks.types.boxed_boolean.BoxedBoolean"]
    """<p>Whether the zonal shift is enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ZonalShiftConfigResponse) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> ZonalShiftConfigResponse:
    out: ZonalShiftConfigResponse = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    return out
