"""Generated from Smithy shape ``com.amazonaws.inspector2#DisableResourceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.resource_scan_type

DisableResourceTypeList: TypeAlias = list[
    "aws_sdk_inspector2.types.resource_scan_type.ResourceScanType"
]


# --- restJson1 ser/de ---
def serialize_json(value: DisableResourceTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> DisableResourceTypeList:
    return list(data)
