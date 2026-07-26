"""Generated from Smithy shape ``com.amazonaws.eks#AddonVersionInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.addon_version_info

AddonVersionInfoList: TypeAlias = list[
    "capo_eks.types.addon_version_info.AddonVersionInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: AddonVersionInfoList) -> list:
    import capo_eks.types.addon_version_info

    out: list = []
    for item in value:
        out.append(capo_eks.types.addon_version_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> AddonVersionInfoList:
    import capo_eks.types.addon_version_info

    out: AddonVersionInfoList = []
    for item in data:
        out.append(capo_eks.types.addon_version_info.deserialize_json(item))
    return out
