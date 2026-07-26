"""Generated from Smithy shape ``com.amazonaws.location#AppleAppList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.apple_app

AppleAppList: TypeAlias = list["capo_location.types.apple_app.AppleApp"]


# --- restJson1 ser/de ---
def serialize_json(value: AppleAppList) -> list:
    import capo_location.types.apple_app

    out: list = []
    for item in value:
        out.append(capo_location.types.apple_app.serialize_json(item))
    return out


def deserialize_json(data: list) -> AppleAppList:
    import capo_location.types.apple_app

    out: AppleAppList = []
    for item in data:
        out.append(capo_location.types.apple_app.deserialize_json(item))
    return out
