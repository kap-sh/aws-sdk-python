"""Generated from Smithy shape ``com.amazonaws.greengrassv2#InstalledComponentLifecycleStatusCodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.installed_component_lifecycle_status_code

InstalledComponentLifecycleStatusCodeList: TypeAlias = list[
    "aws_sdk_greengrassv2.types.installed_component_lifecycle_status_code.InstalledComponentLifecycleStatusCode"
]


# --- restJson1 ser/de ---
def serialize_json(value: InstalledComponentLifecycleStatusCodeList) -> list:
    return list(value)


def deserialize_json(data: list) -> InstalledComponentLifecycleStatusCodeList:
    return list(data)
