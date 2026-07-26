"""Generated from Smithy shape ``com.amazonaws.inspector2#EnableResourceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.resource_scan_type

EnableResourceTypeList: TypeAlias = list[
    "capo_inspector2.types.resource_scan_type.ResourceScanType"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnableResourceTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> EnableResourceTypeList:
    return list(data)
