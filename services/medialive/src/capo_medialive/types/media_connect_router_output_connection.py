"""Generated from Smithy shape ``com.amazonaws.medialive#MediaConnectRouterOutputConnection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class MediaConnectRouterOutputConnection(TypedDict, closed=True):
    router_input_arn: NotRequired["capo_medialive.types.__string.__string"]
    """The ARN of the MediaConnect Router Input connected to this pipeline."""


# --- restJson1 ser/de ---
def serialize_json(value: MediaConnectRouterOutputConnection) -> dict:
    out: dict = {}
    if "router_input_arn" in value:
        out["routerInputArn"] = value["router_input_arn"]
    return out


def deserialize_json(data: dict) -> MediaConnectRouterOutputConnection:
    out: MediaConnectRouterOutputConnection = {}  # type: ignore[typeddict-item]
    if "routerInputArn" in data:
        out["router_input_arn"] = data["routerInputArn"]
    return out
