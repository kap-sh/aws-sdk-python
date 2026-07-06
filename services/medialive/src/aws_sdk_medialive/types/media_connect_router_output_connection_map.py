"""Generated from Smithy shape ``com.amazonaws.medialive#MediaConnectRouterOutputConnectionMap``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class MediaConnectRouterOutputConnectionMap(TypedDict, closed=True):
    pipeline0: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The ARN of the MediaConnect Router Input connected to pipeline 0."""
    pipeline1: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The ARN of the MediaConnect Router Input connected to pipeline 1."""


# --- restJson1 ser/de ---
def serialize_json(value: MediaConnectRouterOutputConnectionMap) -> dict:
    out: dict = {}
    if "pipeline0" in value:
        out["pipeline0"] = value["pipeline0"]
    if "pipeline1" in value:
        out["pipeline1"] = value["pipeline1"]
    return out


def deserialize_json(data: dict) -> MediaConnectRouterOutputConnectionMap:
    out: MediaConnectRouterOutputConnectionMap = {}  # type: ignore[typeddict-item]
    if "pipeline0" in data:
        out["pipeline0"] = data["pipeline0"]
    if "pipeline1" in data:
        out["pipeline1"] = data["pipeline1"]
    return out
