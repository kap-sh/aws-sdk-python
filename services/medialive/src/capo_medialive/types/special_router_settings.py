"""Generated from Smithy shape ``com.amazonaws.medialive#SpecialRouterSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class SpecialRouterSettings(TypedDict, closed=True):
    router_arn: NotRequired["capo_medialive.types.__string.__string"]
    """This is the arn of the MediaConnect Router resource being associated with the MediaLive Input."""


# --- restJson1 ser/de ---
def serialize_json(value: SpecialRouterSettings) -> dict:
    out: dict = {}
    if "router_arn" in value:
        out["routerArn"] = value["router_arn"]
    return out


def deserialize_json(data: dict) -> SpecialRouterSettings:
    out: SpecialRouterSettings = {}  # type: ignore[typeddict-item]
    if "routerArn" in data:
        out["router_arn"] = data["routerArn"]
    return out
