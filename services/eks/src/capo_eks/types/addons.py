"""Generated from Smithy shape ``com.amazonaws.eks#Addons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.addon_info

Addons: TypeAlias = list["capo_eks.types.addon_info.AddonInfo"]


# --- restJson1 ser/de ---
def serialize_json(value: Addons) -> list:
    import capo_eks.types.addon_info

    out: list = []
    for item in value:
        out.append(capo_eks.types.addon_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> Addons:
    import capo_eks.types.addon_info

    out: Addons = []
    for item in data:
        out.append(capo_eks.types.addon_info.deserialize_json(item))
    return out
