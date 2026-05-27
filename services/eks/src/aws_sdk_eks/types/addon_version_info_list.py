"""Generated from Smithy shape ``com.amazonaws.eks#AddonVersionInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eks.types.addon_version_info

AddonVersionInfoList: TypeAlias = list[
    "aws_sdk_eks.types.addon_version_info.AddonVersionInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: AddonVersionInfoList) -> list:
    import aws_sdk_eks.types.addon_version_info

    out: list = []
    for item in value:
        out.append(aws_sdk_eks.types.addon_version_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> AddonVersionInfoList:
    import aws_sdk_eks.types.addon_version_info

    out: AddonVersionInfoList = []
    for item in data:
        out.append(aws_sdk_eks.types.addon_version_info.deserialize_json(item))
    return out
